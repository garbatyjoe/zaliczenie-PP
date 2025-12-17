import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests

def wczytaj_zdjecie(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        img_bgr = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        
        if img_bgr is None:
            return None
            
        return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    except Exception:
        return None

def analizuj_jakosc(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    mean_val, std_dev = cv2.meanStdDev(gray)
    mean_val = mean_val[0][0]
    std_dev = std_dev[0][0]
    
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    pixels_black = hist[0][0]
    pixels_white = hist[255][0]
    total_pixels = img.shape[0] * img.shape[1]
    
    clipping_shadows = (pixels_black / total_pixels) * 100
    clipping_highlights = (pixels_white / total_pixels) * 100
    
    diagnoza = []
    wymaga_poprawy = False

    if mean_val < 60:
        diagnoza.append("Niedoświetlone (za ciemne)")
        wymaga_poprawy = True
    elif mean_val > 195:
        diagnoza.append("Prześwietlone (za jasne)")
        wymaga_poprawy = True
        
    if std_dev < 30:
        diagnoza.append("Bardzo niski kontrast")
        wymaga_poprawy = True
    elif std_dev < 50:
        diagnoza.append("Umiarkowany kontrast")
        
    if clipping_shadows > 1.0:
        diagnoza.append(f"Utrata cieni ({clipping_shadows:.1f}%)")
    if clipping_highlights > 1.0:
        diagnoza.append(f"Utrata świateł ({clipping_highlights:.1f}%)")
        
    if not diagnoza:
        diagnoza.append("Ekspozycja poprawna")

    return {
        "srednia": mean_val,
        "odchylenie": std_dev,
        "diagnoza": diagnoza,
        "wymaga_poprawy": wymaga_poprawy
    }

def popraw_jakosc_clahe(img):
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l_improved = clahe.apply(l)
    
    lab_improved = cv2.merge((l_improved, a, b))
    return cv2.cvtColor(lab_improved, cv2.COLOR_LAB2RGB)

def prezentuj_wyniki(img, stats):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    ax = axes.ravel()
    
    ax[0].imshow(img)
    ax[0].set_title("Oryginał")
    ax[0].axis('off')
    
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    hist_lum = cv2.calcHist([gray], [0], None, [256], [0, 256])
    ax[1].plot(hist_lum, color='black')
    ax[1].fill_between(range(256), hist_lum.flatten(), color='gray', alpha=0.3)
    ax[1].set_title("Histogram Jasności")
    ax[1].set_xlim([0, 256])
    ax[1].grid(alpha=0.3)
    
    colors = ('r', 'g', 'b')
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        ax[2].plot(hist, color=color, alpha=0.8)
    ax[2].set_title("Histogramy RGB")
    ax[2].set_xlim([0, 256])
    ax[2].grid(alpha=0.3)
    
    text_content = "WYNIKI ANALIZY:\n\n"
    text_content += f"Srednia jasnosc: {stats['srednia']:.2f}\n"
    text_content += f"Kontrast (StdDev): {stats['odchylenie']:.2f}\n\n"
    text_content += "Diagnoza:\n" + "\n".join([f"- {d}" for d in stats['diagnoza']])
    
    ax[3].axis('off')
    ax[3].text(0.05, 0.9, text_content, fontsize=11, verticalalignment='top', family='monospace')
    
    plt.tight_layout()
    plt.show()

# --- GLOWNA SEKCJA ---

URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Atelier_de_formation_et_de_t%C3%A9l%C3%A9versement_Wikim%C3%A9dia_Commons_2.jpg/1280px-Atelier_de_formation_et_de_t%C3%A9l%C3%A9versement_Wikim%C3%A9dia_Commons_2.jpg"

print(f"Pobieranie: {URL}")
obraz = wczytaj_zdjecie(URL)

if obraz is not None:
    statystyki = analizuj_jakosc(obraz)
    prezentuj_wyniki(obraz, statystyki)
    
    print("\n--- KONSOLA ---")
    print(f"Średnia: {statystyki['srednia']:.2f}, Odchylenie: {statystyki['odchylenie']:.2f}")
    print("Diagnoza:", statystyki['diagnoza'])
    
    if statystyki['wymaga_poprawy']:
        print("Wykryto problemy. Uruchamiam korekcję CLAHE...")
        obraz_poprawiony = popraw_jakosc_clahe(obraz)
        
        statystyki_po = analizuj_jakosc(obraz_poprawiony)
        
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.imshow(obraz)
        plt.title("Przed")
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(obraz_poprawiony)
        plt.title("Po korekcji CLAHE")
        plt.axis('off')
        plt.show()
else:
    print("Błąd pobierania zdjęcia.")