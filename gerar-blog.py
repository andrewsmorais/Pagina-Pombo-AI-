# Gera o blog do Pombo AI (espanhol). Rode: python3 gerar-blog.py
# Dados nutricionais: USDA FoodData Central, SR Legacy (abril 2018), valores por 100 g.
import os, json, html, re

ROOT = os.path.dirname(os.path.abspath(__file__))
DOM = "https://www.SEU-DOMINIO.com.br"
FECHA = "2026-11-12"; FECHA_TXT = "12 nov 2026"
E = html.escape

# kcal, proteína, hidratos, grasa, fibra por 100 g (USDA SR Legacy, fdc_id)
U = {
 173801: ("Garbanzos cocidos en conserva, escurridos", 138, 7.04, 22.87, 2.47, 6.3),
 171986: ("Atún claro al natural, escurrido", 116, 25.51, 0, 0.82, 0),
 170108: ("Pimiento rojo", 26, 0.99, 6.03, 0.3, 2.1),
 170000: ("Cebolla", 40, 1.1, 9.34, 0.1, 1.7),
 171413: ("Aceite de oliva", 884, 0, 0, 100, 0),
 167747: ("Zumo de limón", 22, 0.35, 6.9, 0.24, 0.3),
 171287: ("Huevo entero", 143, 12.56, 0.72, 9.51, 0),
 172183: ("Clara de huevo", 52, 10.9, 0.73, 0.17, 0),
 169291: ("Calabacín", 17, 1.21, 3.11, 0.32, 1.0),
 168462: ("Espinacas", 23, 2.86, 3.63, 0.39, 2.2),
 169295: ("Calabaza", 45, 1.0, 11.69, 0.1, 2.0),
 170393: ("Zanahoria", 41, 0.93, 9.58, 0.24, 2.8),
 169246: ("Puerro", 61, 1.5, 14.15, 0.3, 1.8),
 170026: ("Patata", 77, 2.05, 17.49, 0.09, 2.1),
 171284: ("Yogur natural", 61, 3.47, 4.66, 3.25, 0),
 171077: ("Pechuga de pollo cruda", 120, 22.5, 0, 2.62, 0),
 169961: ("Judías verdes", 31, 1.83, 6.97, 0.22, 2.7),
 169230: ("Ajo", 149, 6.36, 33.06, 0.5, 2.1),
 172420: ("Lentejas crudas", 352, 24.63, 63.35, 1.06, 10.7),
 170457: ("Tomate", 18, 0.88, 3.89, 0.2, 1.2),
 168878: ("Arroz blanco cocido", 130, 2.69, 28.17, 0.28, 0.4),
 168877: ("Arroz blanco crudo", 365, 7.13, 79.95, 0.66, 1.3),
 171705: ("Aguacate", 160, 2.0, 8.53, 14.66, 6.7),
 169214: ("Maíz dulce en conserva", 67, 2.29, 14.34, 1.22, 2.0),
 172688: ("Pan integral", 252, 12.45, 42.71, 3.5, 6.0),
 175167: ("Salmón atlántico de piscifactoría", 208, 20.42, 0, 13.42, 0),
 173944: ("Plátano", 89, 1.09, 22.84, 0.33, 2.6),
 173904: ("Copos de avena", 379, 13.15, 67.7, 6.52, 10.1),
 171304: ("Yogur griego natural", 97, 9.0, 3.98, 5.0, 0),
 171267: ("Leche semidesnatada (2 %)", 50, 3.3, 4.8, 1.98, 0),
 171955: ("Bacalao atlántico (referencia para bacalao desalado)", 82, 17.81, 0, 0.67, 0),
 170016: ("Guisantes congelados", 77, 5.22, 13.62, 0.4, 4.5),
 168894: ("Harina de trigo", 364, 10.33, 76.31, 0.98, 2.7),
 170416: ("Perejil fresco", 36, 2.97, 6.33, 0.79, 3.3),
 169247: ("Lechuga romana", 17, 1.23, 3.29, 0.3, 2.1),
 169094: ("Aceitunas negras", 116, 0.84, 6.04, 10.9, 1.6),
}

def nutr(ings, rac):
    t = [0, 0, 0, 0, 0]
    for _, g, fid in ings:
        if fid is None: continue
        v = U[fid]
        for i in range(5): t[i] += v[i + 1] * g / 100
    return [x / rac for x in t]

def sellos(n):
    kcal, p, hc, gr, fi = n
    s = []
    if kcal and p * 4 / kcal >= .20: s.append("Alta en proteínas")
    elif kcal and p * 4 / kcal >= .12: s.append("Fuente de proteínas")
    if kcal and fi / kcal * 100 >= 3: s.append("Alta en fibra")
    elif kcal and fi / kcal * 100 >= 1.5: s.append("Fuente de fibra")
    return s

def receta(r):
    n = nutr(r["ing"], r["rac"])
    kcal, p, hc, gr, fi = n
    tot = p * 4 + hc * 4 + gr * 9 or 1
    pp, ph, pg = round(p * 4 / tot * 100), round(hc * 4 / tot * 100), 0
    pg = 100 - pp - ph
    ing = "".join(f"<li>{E(t)}</li>" for t, _, _ in r["ing"])
    pasos = "".join(f"<li>{E(x)}</li>" for x in r["pasos"])
    sel = "".join(f'<span class="sello">{s}</span>' for s in sellos(n))
    foto = "" if r.get("sin_foto") else f'<figure class="receta-foto"><img src="../assets/blog/{r["img"]}.jpg" alt="{E(r["alt"])}" width="1200" height="900" loading="lazy"><figcaption>{E(r.get("cap","Foto: Unsplash"))}</figcaption></figure>'
    return f"""
<section class="receta" id="{r['id']}">
{foto}
<h2>{E(r['t'])}</h2>
<p class="receta-meta"><span>🍽 {r['rac']} {'ración' if r['rac']==1 else 'raciones'}</span><span>⏱ {r['min']} min</span>{sel}</p>
<p>{r['intro']}</p>
<div class="receta-cols">
<div><h3>Ingredientes</h3><ul class="ingredientes">{ing}</ul></div>
<div class="nutri"><h3>Información nutricional <small>por ración</small></h3>
<div class="kcal"><strong>{kcal:.0f}</strong> kcal</div>
<div class="barra" role="img" aria-label="Reparto de energía: proteínas {pp} %, hidratos {ph} %, grasas {pg} %"><span class="b-p" style="width:{pp}%"></span><span class="b-h" style="width:{ph}%"></span><span class="b-g" style="width:{pg}%"></span></div>
<table><tbody>
<tr><th><i class="pt p"></i>Proteínas</th><td>{p:.0f} g</td><td>{pp} %</td></tr>
<tr><th><i class="pt h"></i>Hidratos de carbono</th><td>{hc:.0f} g</td><td>{ph} %</td></tr>
<tr><th><i class="pt g"></i>Grasas</th><td>{gr:.0f} g</td><td>{pg} %</td></tr>
<tr><th>Fibra</th><td>{fi:.0f} g</td><td></td></tr>
</tbody></table>
<p class="nota-n">El % indica de dónde viene la energía del plato.</p>
</div></div>
<h3>Preparación</h3><ol class="pasos">{pasos}</ol>
<div class="aporta"><h3>Lo que aporta</h3><p>{r['aporta']}</p></div>
</section>"""

NOTA_N = ('<div class="aviso"><p><strong>Cómo calculamos los valores:</strong> sumamos los ingredientes con la base pública del USDA (FoodData Central, SR Legacy) y dividimos entre las raciones. '
          'Son aproximaciones: cambian según la marca, el tamaño y la cocción. Los sellos "fuente de" y "alta en" siguen los criterios del Reglamento (CE) 1924/2006. '
          'Para saber lo que comes de verdad, haz una foto a tu plato con <a href="../index.html">Pombo AI</a>.</p></div>')
AV_SALUD = "Este artículo es informativo y no sustituye el consejo de un médico o dietista-nutricionista. Si tienes una enfermedad, tomas medicación, estás embarazada o has tenido un trastorno de la conducta alimentaria, consulta con un profesional antes de cambiar tu alimentación."
APP_AYUNO = ('<div class="app-caja"><img src="../assets/pombo-icon.png" alt="" width="56" height="56"><div><p><strong>Controla tu ayuno con Pombo AI</strong></p>'
             '<p>El temporizador de ayuno del app tiene planes 14:10, 16:8, 18:6 y 20:4, o uno personalizado de 1 a 48 horas. Te avisa al terminar, guarda tu historial y puedes exportarlo en PDF o CSV. Cuando rompas el ayuno, haz una foto a tu plato para registrar calorías y macros.</p>'
             '<p><a class="boton" href="../index.html">Descubre Pombo AI</a></p></div></div>')
APP_FOTO = ('<div class="app-caja"><img src="../assets/pombo-icon.png" alt="" width="56" height="56"><div><p><strong>¿Cuánto comes de verdad?</strong></p>'
            '<p>Con Pombo AI haces una foto a tu plato y la inteligencia artificial estima calorías, proteínas, hidratos y grasas en segundos. Es una estimación orientativa, no un dato médico.</p>'
            '<p><a class="boton" href="../index.html">Descubre Pombo AI</a></p></div></div>')

def fig(img, alt, cap="Foto: Unsplash"):
    return f'<figure class="foto-art"><img src="../assets/blog/{img}.jpg" alt="{E(alt)}" width="1200" height="900" loading="lazy"><figcaption>{E(cap)}</figcaption></figure>'

A = []
def art(**k): A.append(k)

# ---------------------------------------------------------------- RECETAS DE BACALAO
BAC = [
 dict(id="bacalao-salsa-verde", img="c1", sin_foto=True, alt="Lomo de pescado blanco con patatas en salsa verde", t="Bacalao en salsa verde con patatas", rac=4, min=40,
  intro="Un clásico vasco que se hace con pocos ingredientes. La salsa se espesa con la gelatina del propio bacalao y un poco de harina.",
  ing=[("600 g de lomos de bacalao desalado",600,171955),("500 g de patatas",500,170026),("100 g de guisantes",100,170016),("30 g de aceite de oliva virgen extra (3 cucharadas)",30,171413),("3 dientes de ajo (12 g)",12,169230),("10 g de harina (1 cucharada)",10,168894),("Un buen puñado de perejil picado (15 g)",15,170416),("Agua o caldo de pescado",0,None)],
  pasos=["Pela las patatas, córtalas en rodajas gruesas y cuécelas 12 minutos en agua con sal. Resérvalas.","En una cazuela baja, dora el ajo laminado en el aceite a fuego suave sin que se queme.","Añade la harina, remueve un minuto y vierte poco a poco un vaso de agua o caldo sin dejar de mover.","Coloca los lomos de bacalao con la piel hacia arriba, añade los guisantes y mueve la cazuela en vaivén durante 8 a 10 minutos para que la salsa ligue.","Incorpora las patatas y el perejil, deja 2 minutos más y sirve."],
  aporta="El bacalao es un pescado blanco muy magro: casi toda su energía viene de la proteína. Las patatas y los guisantes aportan hidratos y algo de fibra, así que es un plato completo para comer."),
 dict(id="bacalao-horno", img="c3", alt="Lomo de pescado blanco al horno con verduras", cap="Imagen ilustrativa. Foto: Unsplash", t="Bacalao al horno con patatas, pimiento y tomate", rac=4, min=50,
  intro="Todo en una bandeja: las verduras se asan primero y el bacalao se termina encima en pocos minutos para que quede jugoso.",
  ing=[("600 g de lomos de bacalao desalado",600,171955),("600 g de patatas",600,170026),("1 pimiento rojo (150 g)",150,170108),("2 tomates (250 g)",250,170457),("1 cebolla (150 g)",150,170000),("25 g de aceite de oliva virgen extra",25,171413),("2 dientes de ajo (8 g)",8,169230),("Pimentón dulce, sal y pimienta",0,None)],
  pasos=["Precalienta el horno a 200 °C.","Corta las patatas en rodajas finas y la cebolla y el pimiento en tiras. Mézclalos en una bandeja con la mitad del aceite, sal y pimentón.","Hornea 25 minutos, hasta que las patatas estén casi tiernas.","Añade el tomate en gajos y coloca encima los lomos de bacalao. Riega con el resto del aceite y el ajo picado.","Hornea 10 a 12 minutos más, según el grosor de los lomos."],
  aporta="Las patatas y las verduras aportan los hidratos y la fibra, y el bacalao suma proteína con muy poca grasa. Una buena opción para una cena de horno sin complicaciones."),
 dict(id="ensalada-garbanzos-bacalao", img="c9", alt="Ensalada de garbanzos con verduras en un cuenco", cap="Imagen ilustrativa. Foto: Unsplash", t="Ensalada de garbanzos con bacalao", rac=2, min=15,
  intro="Una ensalada fresca de verano que junta legumbre y pescado. Si usas garbanzos de bote, está lista en un cuarto de hora.",
  ing=[("240 g de garbanzos cocidos, escurridos",240,173801),("150 g de bacalao desalado en migas",150,171955),("1 tomate grande (150 g)",150,170457),("80 g de lechuga romana",80,169247),("½ cebolla tierna (50 g)",50,170000),("30 g de aceitunas negras",30,169094),("15 g de aceite de oliva virgen extra",15,171413),("Vinagre, sal y pimienta",0,None)],
  pasos=["Escalda las migas de bacalao 1 minuto en agua caliente y escúrrelas, o úsalas crudas si están bien desaladas.","Enjuaga los garbanzos y mézclalos con el tomate en dados, la cebolla en juliana y las aceitunas.","Sirve sobre la lechuga, añade el bacalao y aliña con aceite, vinagre y pimienta. Prueba antes de poner sal: el bacalao ya la lleva."],
  aporta="Garbanzos y bacalao se reparten el trabajo: la legumbre aporta hidratos y fibra, y el pescado, proteína magra. Es una comida que sacia mucho para las calorías que tiene."),
]
art(slug="recetas-de-bacalao-faciles-y-saludables", cat="Recetas", img="c1",
 title="3 recetas de bacalao fáciles y saludables (con su información nutricional)",
 desc="Bacalao en salsa verde, al horno con verduras y en ensalada con garbanzos. Tres recetas fáciles con calorías, proteínas e hidratos por ración.",
 mins=8,
 faq=[("¿Cuánto tiempo hay que desalar el bacalao?","Depende del grosor: las migas necesitan menos tiempo y los lomos gruesos más. Sigue las indicaciones del envase y cambia el agua varias veces, siempre en la nevera. Si lo compras ya desalado, te ahorras este paso."),
      ("¿El bacalao engorda?","El bacalao es un pescado blanco muy magro. Según la base del USDA, 100 g de bacalao atlántico crudo aportan unas 82 kcal y casi 18 g de proteína. Lo que más cambia las calorías del plato es el aceite y la guarnición.")],
 body=f"""
<p class="entradilla">El bacalao es uno de los pescados más queridos en España. Desalado es un pescado blanco magro, con mucha proteína y casi nada de grasa. Aquí tienes tres formas de prepararlo, con la información nutricional de cada plato.</p>
<div class="aviso"><p><strong>Sobre la sal:</strong> el bacalao salado lleva mucha sal. Desálalo bien o cómpralo ya desalado, y no añadas sal hasta probar el plato. Para los cálculos usamos los valores del bacalao atlántico crudo del USDA como referencia del bacalao bien desalado; el sodio real dependerá del desalado.</p></div>
<nav class="indice-recetas" aria-label="Recetas"><p><strong>En este artículo:</strong></p><ol>{''.join(f'<li><a href="#{r["id"]}">{E(r["t"])}</a></li>' for r in BAC)}</ol></nav>
{''.join(receta(r) for r in BAC)}
{NOTA_N}
<p>¿Quieres saber más sobre por qué conviene comer pescado varias veces por semana? Lee <a href="beneficios-del-pescado-cuanto-comer.html">los beneficios del pescado y cuánto comer a la semana</a>.</p>
{APP_FOTO}
""",
 fuentes=[("USDA FoodData Central, SR Legacy (base de composición de alimentos)","https://fdc.nal.usda.gov/")])

# ---------------------------------------------------------------- BENEFICIOS DEL PESCADO
pes_tabla = "".join(f"<tr><th>{n}</th><td>{U[i][1]}</td><td>{U[i][2]:.1f} g</td><td>{U[i][4]:.1f} g</td></tr>" for n,i in [("Bacalao atlántico (crudo)",171955),("Salmón atlántico de piscifactoría (crudo)",175167),("Sardinas en aceite, escurridas",None) ] if i)
pes_tabla += "<tr><th>Sardinas en conserva en aceite, escurridas</th><td>208</td><td>24.6 g</td><td>11.5 g</td></tr><tr><th>Atún claro al natural, escurrido</th><td>116</td><td>25.5 g</td><td>0.8 g</td></tr>"
art(slug="beneficios-del-pescado-cuanto-comer", cat="Pescado", img="c8",
 title="Beneficios del pescado: cuánto comer a la semana y cuál elegir",
 desc="Qué recomienda la AESAN sobre el consumo de pescado, la diferencia entre pescado blanco y azul, y qué especies deben evitar embarazadas y niños por el mercurio.",
 mins=6,
 faq=[("¿Cuántas veces a la semana hay que comer pescado?","Las recomendaciones dietéticas de la AESAN de 2022 proponen 3 o más raciones de pescado a la semana, priorizando el pescado azul. Una ración son 125 a 150 g."),
      ("¿Qué pescados no deben comer las embarazadas?","Por su alto contenido en mercurio, la AESAN recomienda que las embarazadas, las mujeres que planean estarlo o en lactancia y los niños de 0 a 10 años eviten el pez espada o emperador, el tiburón, el atún rojo y el lucio. Los niños de 10 a 14 años deben limitarlos a 120 g al mes."),
      ("¿El atún en lata tiene mucho mercurio?","Las conservas de atún no se hacen con atún rojo, que es la especie con más mercurio, así que según Consumer los niños pueden comer atún en lata dentro de las 3 o 4 raciones semanales de pescado de contenido bajo o medio.")],
 body=f"""
<p class="entradilla">España es un país de pescado, pero no siempre sabemos cuánto comer ni cuál elegir. Esto es lo que recomiendan las autoridades sanitarias españolas, explicado de forma sencilla.</p>

<h2>Por qué es buena idea comer pescado</h2>
<p>La AESAN recomienda comer pescado varias veces por semana por sus efectos beneficiosos para la salud y lo considera una pieza fundamental de la dieta mediterránea. Además de proteína de calidad, el pescado aporta vitamina D, yodo y selenio, según recoge la Federación Española de Sociedades de Nutrición (FESNAD), que resume que los beneficios de comerlo superan los riesgos potenciales.</p>
{fig("c12","Sardinas frescas en una bandeja con rodajas de limón")}

<h2>Cuánto pescado comer a la semana</h2>
<p>Las recomendaciones dietéticas de la AESAN de 2022 proponen 3 o más raciones de pescado a la semana, priorizando el pescado azul (sardinas, boquerones, caballa, jurel) y las especies con menor impacto ambiental. Según el resumen de la OCU, una ración son 125 a 150 g.</p>
<p>Las recomendaciones anteriores sobre mercurio hablaban de 3 a 4 raciones a la semana, variando entre pescado blanco y azul. En la práctica, el mensaje es el mismo: pescado varias veces por semana y variado.</p>

<h2>Pescado blanco y pescado azul</h2>
<ul>
<li><strong>Blanco</strong> (bacalao, merluza, lenguado): muy poca grasa y muchas proteínas.</li>
<li><strong>Azul</strong> (sardina, boquerón, caballa, salmón): más grasa, y de ahí más calorías, pero es grasa del propio pescado.</li>
</ul>
<table><thead><tr><th>Por cada 100 g</th><th>kcal</th><th>Proteínas</th><th>Grasas</th></tr></thead><tbody>{pes_tabla}</tbody></table>
<p class="nota-n">Datos: USDA FoodData Central, SR Legacy.</p>
{fig("c7","Lata de sardinas en aceite junto a una botella de aceite")}

<h2>El mercurio: quién debe tener cuidado</h2>
<p>La AESAN actualizó en 2019 sus recomendaciones por el mercurio. Las embarazadas, las mujeres que planean estarlo o en lactancia y los niños de 0 a 10 años deben evitar el pez espada o emperador, el tiburón, el atún rojo y el lucio, pero mantener 3 o 4 raciones a la semana de especies con contenido bajo o medio. Los niños de 10 a 14 años deben limitar esas cuatro especies a 120 g al mes.</p>
<p>Para el resto de la población no hay restricciones especiales: la recomendación es comer pescado variado. Las conservas de atún, por ejemplo, no se hacen con atún rojo.</p>

<h2>Ideas para comer más pescado</h2>
<ol>
<li>Ten latas de sardinas, caballa o atún al natural para ensaladas rápidas.</li>
<li>Prueba el pescado congelado: es práctico y conserva bien sus nutrientes.</li>
<li>Cocina al horno, a la plancha o en papillote para no añadir mucha grasa.</li>
<li>Busca recetas tradicionales, como nuestras <a href="recetas-de-bacalao-faciles-y-saludables.html">3 recetas de bacalao</a>.</li>
</ol>
{fig("c10","Mercado de pescado con puestos de pescado fresco sobre hielo")}
{APP_FOTO}
""",
 fuentes=[("AESAN (2022). Recomendaciones dietéticas saludables y sostenibles. Nota de prensa de La Moncloa","https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/consumo/paginas/2022/90922-garzon-recomendaciones-aesan.aspx"),
  ("OCU. Nuevas recomendaciones dietéticas de la AESAN","https://www.ocu.org/alimentacion/comer-bien/noticias/recomendaciones-dieteticas-aesan"),
  ("Comunidad de Madrid. Mercurio en el pescado","https://www.comunidad.madrid/salud/mercurio-pescado"),
  ("FESNAD. Pescado y salud (díptico 2022)","https://fesnad.org/resources/files/DNN/2022/diptico.pdf"),
  ("Consumer. Pescado y mercurio: todo lo que debes saber","https://www.consumer.es/?p=118478"),
  ("USDA FoodData Central, SR Legacy","https://fdc.nal.usda.gov/")])

# ---------------------------------------------------------------- ROMPER EL AYUNO
art(slug="que-comer-al-romper-el-ayuno", cat="Ayuno", img="ayuno-romper",
 title="Qué comer al romper el ayuno: ideas sencillas y errores que conviene evitar",
 desc="Cómo romper el ayuno intermitente sin darte un atracón: qué poner en el plato, ideas de comidas y cómo llevar el control con el temporizador de Pombo AI.",
 mins=5,
 faq=[("¿Qué es lo primero que debo comer al romper el ayuno?","No hay un alimento obligatorio. Una comida normal y equilibrada, con proteína, verdura y una fuente de hidratos, suele funcionar mejor que lanzarse a picar lo primero que haya."),
      ("¿Puedo comer lo que quiera en la ventana de alimentación?","Según la OCU, los estudios no muestran una gran diferencia entre ayunar y seguir una dieta de restricción calórica convencional, así que lo que comes en la ventana sigue contando.")],
 body=f"""
<p class="entradilla">El ayuno termina y llega el momento clave: la primera comida. Si llegas con mucha hambre es fácil comer deprisa y de más. Estas ideas te ayudan a romperlo con cabeza.</p>

<h2>Lo que dice la evidencia</h2>
<p>Las revisiones más recientes coinciden en que el ayuno intermitente no hace milagros. La revisión Cochrane de 2026 encontró poca o ninguna diferencia de peso frente al asesoramiento dietético tradicional, y la OCU recuerda que los estudios no muestran una gran diferencia entre ayunar y reducir calorías de forma convencional. Por eso, lo que comes cuando rompes el ayuno importa tanto como las horas que ayunas.</p>

<h2>Cómo montar el plato</h2>
<ul>
<li><strong>Proteína:</strong> huevos, legumbres, pescado, pollo o yogur natural.</li>
<li><strong>Verdura u hortaliza:</strong> la mitad del plato si es posible.</li>
<li><strong>Hidratos de calidad:</strong> pan integral, arroz, patata, avena o fruta.</li>
<li><strong>Un poco de grasa:</strong> aceite de oliva, aguacate o frutos secos.</li>
<li><strong>Agua</strong> como bebida principal.</li>
</ul>
{fig("ayuno-romper2","Desayuno con fruta, tostadas y aguacate sobre una mesa de madera")}

<h2>Ideas de comidas para romper el ayuno</h2>
<ol>
<li>Tostada integral con huevo y espinacas (receta en <a href="recetas-para-ganar-masa-muscular-proteina.html#tostada-huevo">ganar masa muscular</a>).</li>
<li>Ensalada templada de garbanzos con atún (<a href="recetas-saludables-para-adelgazar-sobrepeso.html#ensalada-garbanzos-atun">ver receta</a>).</li>
<li>Batido de plátano, avena y yogur, si prefieres algo suave (<a href="recetas-para-ganar-masa-muscular-proteina.html#batido-platano-avena">ver receta</a>).</li>
<li>Bacalao en salsa verde con patatas para una comida completa (<a href="recetas-de-bacalao-faciles-y-saludables.html#bacalao-salsa-verde">ver receta</a>).</li>
</ol>

<h2>Errores frecuentes</h2>
<ul>
<li><strong>Compensar con ultraprocesados:</strong> bollería, snacks o refrescos anulan buena parte del esfuerzo.</li>
<li><strong>Comer muy rápido:</strong> sirve el plato, siéntate y tómate tu tiempo.</li>
<li><strong>Olvidar beber:</strong> durante el ayuno se permiten agua, café solo e infusiones sin azúcar.</li>
<li><strong>Forzar ayunos largos:</strong> si te encuentras mal, para y consulta con un profesional.</li>
</ul>
{APP_AYUNO}
""",
 fuentes=[("Cochrane (2026). Ayuno intermitente para el tratamiento del sobrepeso y la obesidad","https://www.cochrane.org/es/node/11572"),
  ("OCU. Ayuno para adelgazar","https://www.ocu.org/alimentacion/adelgazar/informe/ayuno-para-adelgazar")])

# ---------------------------------------------------------------- RECETAS ADELGAZAR
ADE = [
 dict(id="ensalada-garbanzos-atun", img="r-garbanzos", alt="Garbanzos cocidos con verduras picadas", t="Ensalada templada de garbanzos con atún y pimiento", rac=2, min=15,
  intro="Legumbre, pescado y verdura en un solo plato. Se prepara en un momento con garbanzos de bote.",
  ing=[("240 g de garbanzos cocidos, escurridos y enjuagados",240,173801),("2 latas de atún al natural (160 g escurrido)",160,171986),("1 pimiento rojo asado en tiras (120 g)",120,170108),("½ cebolla roja (50 g)",50,170000),("Zumo de ½ limón (15 g)",15,167747),("1 cucharada de aceite de oliva virgen extra (10 g)",10,171413),("Perejil, sal y pimienta",0,None)],
  pasos=["Calienta los garbanzos 2 minutos en un cazo con un poco de agua y escúrrelos.","Mézclalos con el atún, el pimiento y la cebolla en juliana fina.","Aliña con el limón, el aceite, sal, pimienta y perejil picado."],
  aporta="Mucha proteína gracias al atún y fibra de los garbanzos, dos cosas que ayudan a quedarse lleno. Es un plato con pocas calorías para lo que sacia."),
 dict(id="tortilla-claras-verduras", img="r-tortilla", alt="Tortilla con verduras en un plato azul", t="Tortilla de claras y verduras al horno", rac=2, min=25,
  intro="Mezclar huevos enteros con claras da una tortilla jugosa, con mucha proteína y menos grasa.",
  ing=[("2 huevos enteros (100 g)",100,171287),("4 claras (130 g)",130,172183),("1 calabacín (200 g)",200,169291),("Un puñado de espinacas (60 g)",60,168462),("½ cebolla (60 g)",60,170000),("1 cucharadita de aceite de oliva (5 g)",5,171413),("Sal, pimienta y orégano",0,None)],
  pasos=["Precalienta el horno a 180 °C.","Sofríe la cebolla y el calabacín en dados con el aceite hasta que estén tiernos. Añade las espinacas al final.","Bate los huevos con las claras, sal y especias, y mézclalos con las verduras.","Vierte en un molde apto para horno y hornea unos 15 minutos, hasta que cuaje."],
  aporta="Es uno de los platos con más proteína por caloría de este artículo. Las verduras dan volumen, así que llena el plato sin sumar mucha energía."),
 dict(id="crema-calabaza-zanahoria", img="r-crema", alt="Crema naranja de verduras en un cuenco", t="Crema de calabaza y zanahoria con yogur", rac=3, min=30,
  intro="Una crema suave y dulce que funciona como primer plato o como cena ligera.",
  ing=[("600 g de calabaza pelada",600,169295),("2 zanahorias (200 g)",200,170393),("1 puerro (100 g)",100,169246),("1 patata pequeña (100 g)",100,170026),("1 cucharada de aceite de oliva (10 g)",10,171413),("1 yogur natural (125 g) para servir",125,171284),("Caldo de verduras sin sal o agua, sal y pimienta",0,None)],
  pasos=["Rehoga el puerro picado en el aceite 3 minutos.","Añade la calabaza, la zanahoria y la patata en trozos y cubre con caldo o agua.","Cuece 20 minutos, tritura y ajusta de sal.","Sirve con una cucharada de yogur por encima."],
  aporta="Mucho volumen y pocas calorías: la base son hortalizas con fibra. No es un plato proteico, así que acompáñalo con un segundo de huevo, pescado o legumbre."),
 dict(id="pollo-limon-judias", img="r-pollo", alt="Pechuga de pollo con judías verdes y zanahoria", t="Pollo al limón con judías verdes y zanahoria", rac=2, min=30,
  intro="Una pechuga jugosa y verduras al vapor o salteadas: un plato que nunca falla.",
  ing=[("2 pechugas de pollo (300 g)",300,171077),("200 g de judías verdes",200,169961),("2 zanahorias (150 g)",150,170393),("Zumo y ralladura de 1 limón (20 g)",20,167747),("1 cucharada de aceite de oliva (10 g)",10,171413),("1 diente de ajo (6 g)",6,169230),("Tomillo, sal y pimienta",0,None)],
  pasos=["Marina el pollo 10 minutos con el limón, el ajo picado, tomillo, sal y pimienta.","Cuece al vapor las judías y la zanahoria en rodajas 8 a 10 minutos.","Haz el pollo a la plancha con el aceite, 5 a 6 minutos por cada lado según el grosor.","Sirve el pollo en láminas con las verduras."],
  aporta="Es el plato con más proteína de esta lista y con muy pocos hidratos. Ideal para la cena si buscas algo ligero que sacie."),
 dict(id="lentejas-estofadas", img="r-lentejas", alt="Cuencos con lentejas y otras legumbres secas", t="Lentejas estofadas con verduras", rac=4, min=40,
  intro="Las lentejas de toda la vida, sin chorizo ni panceta. Igual de sabrosas y mucho más ligeras.",
  ing=[("300 g de lentejas pardinas",300,172420),("1 zanahoria (100 g)",100,170393),("1 pimiento rojo (100 g)",100,170108),("1 tomate maduro (150 g)",150,170457),("1 cebolla (100 g)",100,170000),("2 dientes de ajo (6 g)",6,169230),("1 cucharada y media de aceite de oliva (15 g)",15,171413),("Pimentón dulce, laurel y sal",0,None)],
  pasos=["Sofríe la cebolla, el ajo, la zanahoria y el pimiento picados con el aceite 8 minutos.","Añade el tomate rallado y una cucharadita de pimentón.","Incorpora las lentejas lavadas, el laurel y agua que las cubra por dos dedos.","Cuece a fuego suave unos 30 minutos, hasta que estén tiernas, y ajusta de sal."],
  aporta="Mucha fibra y proteína vegetal en un plato económico. Es la receta de este artículo con más hidratos, por lo que da energía para toda la tarde."),
]
art(slug="recetas-saludables-para-adelgazar-sobrepeso", cat="Recetas", img="adelgazar",
 title="5 recetas saludables y saciantes para perder peso sin pasar hambre",
 desc="Cinco recetas fáciles con verdura, legumbres y proteína para comer mejor si tienes sobrepeso. Con calorías, proteínas, hidratos y grasas por ración.",
 mins=9,
 faq=[("¿Qué debe tener una comida para saciar?","Combinar proteína (huevo, pescado, legumbres, pollo), fibra (verdura, legumbres, integrales) y una grasa saludable en cantidad moderada ayuda a sentirse lleno con menos calorías.")],
 body=f"""
<p class="entradilla">Perder peso no pasa por comer poco, sino por comer bien: platos con mucha verdura, proteína y fibra que sacian. Estas cinco recetas son sencillas, económicas y fáciles de repetir. Cada una lleva su tabla nutricional por ración.</p>
<nav class="indice-recetas" aria-label="Recetas"><p><strong>En este artículo:</strong></p><ol>{''.join(f'<li><a href="#{r["id"]}">{E(r["t"])}</a></li>' for r in ADE)}</ol></nav>
{''.join(receta(r) for r in ADE)}
{NOTA_N}
<h2>Trucos para que funcione</h2>
<ol>
<li>Llena la mitad del plato de verdura.</li>
<li>Incluye una fuente de proteína en cada comida.</li>
<li>Sirve en plato llano, no en fuente, y repite solo si sigues con hambre.</li>
<li>Bebe agua y deja los refrescos para ocasiones puntuales.</li>
</ol>
{APP_FOTO}
""",
 fuentes=[("USDA FoodData Central, SR Legacy (base de composición de alimentos)","https://fdc.nal.usda.gov/")])

# ---------------------------------------------------------------- RECETAS MÚSCULO
MUS = [
 dict(id="bowl-pollo-arroz", img="r-bowl", alt="Pollo a la plancha en láminas con arroz y ensalada", t="Bowl de arroz, pollo y aguacate", rac=1, min=20,
  intro="Un plato combinado para después de entrenar: proteína, hidratos para reponer y grasas del aguacate.",
  ing=[("150 g de pechuga de pollo",150,171077),("200 g de arroz cocido (unos 70 g en crudo)",200,168878),("½ aguacate (70 g)",70,171705),("40 g de maíz dulce",40,169214),("80 g de tomate cherry",80,170457),("1 cucharadita de aceite de oliva (5 g)",5,171413),("Limón y sal",0,None)],
  pasos=["Haz el pollo a la plancha con el aceite y córtalo en láminas.","Pon el arroz en la base de un bol.","Añade el pollo, el aguacate en láminas, el maíz y los tomates partidos.","Aliña con limón y una pizca de sal."],
  aporta="Un plato equilibrado: buena cantidad de proteína, hidratos para recuperar el glucógeno tras el entrenamiento y grasas del aguacate."),
 dict(id="tostada-huevo", img="r-revuelto", alt="Tostada de pan integral con huevo a la plancha", t="Tostadas integrales con huevo y espinacas", rac=1, min=10,
  intro="Desayuno o cena en diez minutos, con proteína del huevo y pan integral.",
  ing=[("2 rebanadas de pan integral (70 g)",70,172688),("2 huevos (100 g)",100,171287),("Un puñado de espinacas (40 g)",40,168462),("1 cucharadita de aceite de oliva (5 g)",5,171413),("Sal y pimienta",0,None)],
  pasos=["Tuesta el pan.","Saltea las espinacas 1 minuto en la sartén con el aceite.","Haz los huevos a la plancha o revueltos en la misma sartén.","Sirve las espinacas y los huevos sobre las tostadas."],
  aporta="Proteína del huevo y del pan, más fibra del pan integral. Si buscas más proteína, añade una lata de atún o un yogur griego al lado."),
 dict(id="lentejas-arroz-huevo", img="r-lentejas-arroz", alt="Cuenco con arroz blanco y legumbres con verduras", t="Lentejas con arroz y huevo duro", rac=2, min=35,
  intro="Legumbre y cereal juntos, un clásico barato que da mucha energía para entrenar.",
  ing=[("160 g de lentejas crudas",160,172420),("100 g de arroz crudo",100,168877),("2 huevos cocidos (100 g)",100,171287),("1 zanahoria (80 g)",80,170393),("½ cebolla (80 g)",80,170000),("1 cucharada de aceite de oliva (10 g)",10,171413),("Pimentón y sal",0,None)],
  pasos=["Sofríe la cebolla y la zanahoria picadas en el aceite y añade una cucharadita de pimentón.","Agrega las lentejas lavadas y cubre con agua. Cuece 15 minutos.","Añade el arroz y un poco más de agua si hace falta. Cuece 15 minutos más.","Sirve con el huevo cocido troceado por encima."],
  aporta="Mucha energía y fibra, con proteína de las lentejas y del huevo. Una buena comida para días de entrenamiento intenso."),
 dict(id="salmon-arroz-brocoli", img="r-salmon", alt="Salmón a la plancha con arroz blanco y brócoli", t="Salmón con arroz y brócoli", rac=2, min=25,
  intro="Pescado azul, arroz y verdura: un plato completo que se hace en menos de media hora.",
  ing=[("2 lomos de salmón (300 g)",300,175167),("300 g de arroz cocido",300,168878),("1 brócoli pequeño (250 g)",250,170379 if 170379 in U else 170393),("1 cucharadita de aceite de oliva (5 g)",5,171413),("Limón, eneldo y sal",0,None)],
  pasos=["Cuece el brócoli al vapor 6 minutos.","Haz el salmón a la plancha con el aceite, empezando por la piel, unos 4 minutos por lado.","Sirve con el arroz y el brócoli, y riega con limón y eneldo."],
  aporta="Proteína abundante y la grasa propia del pescado azul. El arroz aporta los hidratos para entrenar y recuperarse."),
 dict(id="batido-platano-avena", img="r-batido", alt="Batido de plátano en un vaso con plátanos y avena", t="Batido de plátano, avena y yogur griego", rac=1, min=5,
  intro="Para después de entrenar o como merienda: se hace en la batidora en cinco minutos.",
  ing=[("1 plátano (120 g)",120,173944),("40 g de copos de avena",40,173904),("1 yogur griego natural (170 g)",170,171304),("200 ml de leche semidesnatada",200,171267),("Canela al gusto",0,None)],
  pasos=["Pon todos los ingredientes en la batidora.","Tritura hasta que quede cremoso y sirve enseguida."],
  aporta="Un aporte cómodo de proteína e hidratos sin cocinar. Útil cuando cuesta llegar a la cantidad de proteína del día."),
]
U[170379] = ("Brócoli", 34, 2.82, 6.64, 0.37, 2.6)
MUS[3]["ing"][2] = ("1 brócoli pequeño (250 g)",250,170379)
art(slug="recetas-para-ganar-masa-muscular-proteina", cat="Recetas", img="musculo",
 title="Recetas para ganar masa muscular: cuánta proteína necesitas y 5 platos fáciles",
 desc="Qué dice la ciencia sobre la proteína para ganar músculo (alrededor de 1,6 g/kg al día) y cinco recetas ricas en proteína con su tabla nutricional.",
 mins=9,
 faq=[("¿Cuánta proteína necesito para ganar músculo?","Un metaanálisis publicado en el British Journal of Sports Medicine con 49 estudios y 1.863 participantes indica que, con suplementación proteica, ingestas superiores a unos 1,6 g/kg al día no aportan más ganancia de masa libre de grasa en entrenamiento de fuerza."),
      ("¿Es imprescindible tomar batidos de proteína?","No. Los batidos son una forma cómoda de llegar a tu cantidad, pero se puede lograr con alimentos como huevos, legumbres, pescado, carne magra y lácteos.")],
 body=f"""
<p class="entradilla">Para ganar músculo hacen falta tres cosas: entrenamiento de fuerza, suficiente proteína y energía para sostenerlo. Aquí tienes qué dice la investigación y cinco recetas con su información nutricional.</p>

<h2>Cuánta proteína necesitas</h2>
<p>Un metaanálisis con metarregresión publicado en el British Journal of Sports Medicine (Morton y colaboradores, 2018) analizó 49 estudios con 1.863 participantes. Concluyó que la suplementación con proteína aumenta de forma significativa la fuerza y el tamaño muscular durante el entrenamiento de fuerza, y que con suplementación las ingestas superiores a unos 1,6 g de proteína por kilo de peso y día no aportan ganancias adicionales de masa libre de grasa.</p>
<p>Para una persona de 75 kg, eso son unos 120 g de proteína al día. Los autores también señalan que el entrenamiento de fuerza es un estímulo mucho más potente que añadir proteína, y que la eficacia de la suplementación disminuye con la edad y aumenta con la experiencia en el entrenamiento.</p>
<div class="aviso"><p>Las personas con enfermedad renal u otras patologías deben consultar con su médico antes de aumentar la proteína.</p></div>
<nav class="indice-recetas" aria-label="Recetas"><p><strong>Las 5 recetas:</strong></p><ol>{''.join(f'<li><a href="#{r["id"]}">{E(r["t"])}</a></li>' for r in MUS)}</ol></nav>
{''.join(receta(r) for r in MUS)}
{NOTA_N}
<h2>Consejos para comer más proteína sin complicarte</h2>
<ol>
<li>Reparte la proteína en 3 o 4 comidas del día.</li>
<li>Mezcla fuentes animales y vegetales: huevos, pescado, lácteos, legumbres, frutos secos.</li>
<li>Come algo más de energía de la que gastas: sin ese pequeño excedente es difícil ganar masa.</li>
<li>Duerme bien y mantén una progresión en tus entrenamientos.</li>
</ol>
{APP_FOTO}
""",
 fuentes=[("Morton R.W. et al. (2018), British Journal of Sports Medicine, 52(6):376-384. PubMed","https://pubmed.ncbi.nlm.nih.gov/28698222/"),
  ("Resumen del estudio de Morton et al. en NutritionInsight","https://www.nutritioninsight.com/news/the-debate-is-over-protein-supplements-significantly-benefit-muscle-mass.html"),
  ("USDA FoodData Central, SR Legacy","https://fdc.nal.usda.gov/")])

# ---------------------------------------------------------------- HIDRATACIÓN
art(slug="hidratacion-ejercicio-cuanta-agua-beber", cat="Hidratación", img="hidratacion",
 title="Hidratación y ejercicio: cuánta agua beber antes, durante y después",
 desc="Guía práctica basada en el consenso del American College of Sports Medicine: pérdida de peso por sudor, cantidades orientativas y riesgos de beber de menos o de más.",
 mins=7,
 faq=[("¿Cuánta agua beber antes de entrenar?","El ACSM sugiere beber despacio unos 5 a 7 mL por kilo de peso corporal al menos 4 horas antes del ejercicio. Si no orinas o la orina es muy oscura, añadir 3 a 5 mL/kg unas 2 horas antes."),
      ("¿Puedo beber demasiada agua haciendo deporte?","Sí. Beber más de lo que sudas puede causar hiponatremia asociada al ejercicio, una bajada de sodio en sangre que puede ser grave."),
      ("¿Cuánto beber después de entrenar?","Para una recuperación rápida tras una deshidratación importante, el ACSM sugiere beber alrededor de 1,5 litros por cada kilo de peso perdido.")],
 body="""
<p class="entradilla">Beber poco al hacer ejercicio perjudica el rendimiento y la salud, pero beber de más también tiene riesgos. Estas son las pautas del American College of Sports Medicine (ACSM) explicadas en claro.</p>
<div class="datos3">
<div><strong>&gt; 2 %</strong><span>de pérdida de peso por sudor es lo que se intenta evitar</span></div>
<div><strong>5–7 mL/kg</strong><span>de líquido al menos 4 horas antes de entrenar</span></div>
<div><strong>≈ 1,5 L</strong><span>por cada kg perdido para recuperarte después</span></div>
</div>
<h2>Por qué importa la hidratación al entrenar</h2>
<p>Sudar es la forma que tiene el cuerpo de enfriarse. Si no repones lo que pierdes, aparece deshidratación. El objetivo del ACSM al beber durante el ejercicio es evitar una deshidratación excesiva y cambios excesivos en el equilibrio de electrolitos. El umbral que se intenta no superar es una pérdida de peso corporal por déficit de agua mayor del 2 %.</p>
<p>Para una persona de 70 kg, un 2 % son 1,4 kg de peso perdido durante la sesión.</p>

<h2>Antes del ejercicio</h2>
<ul>
<li>Bebe despacio unos 5 a 7 mL por kilo de peso corporal, al menos 4 horas antes (para 70 kg, entre 350 y 490 mL).</li>
<li>Si no orinas o la orina es muy oscura, añade 3 a 5 mL por kilo unas 2 horas antes.</li>
</ul>

<h2>Durante el ejercicio</h2>
<p>El ACSM no recomienda guiarse solo por la sed. Propone programas individualizados, calculados pesándote antes y después del ejercicio para estimar tu tasa de sudoración. Como punto de partida para maratonistas bien hidratados, el consenso sugiere beber a voluntad entre 0,4 y 0,8 litros por hora, ajustando según el tamaño corporal, la velocidad y el clima.</p>
<p>En sesiones de menos de una hora a intensidad moderada, normalmente basta con beber agua a sorbos cuando lo necesites.</p>

<h2>Después del ejercicio</h2>
<p>Para recuperarte rápido y por completo tras una deshidratación importante, el ACSM sugiere beber en torno a 1,5 litros por cada kilo de peso perdido. Pesarte antes y después te da la cifra exacta.</p>

<h2>Peligros de no beber lo suficiente</h2>
<ul>
<li>Pérdida de rendimiento y más sensación de esfuerzo.</li>
<li>Dolor de cabeza, mareo y calambres.</li>
<li>Mayor riesgo de golpe de calor al entrenar con mucho calor.</li>
</ul>
<p>Estos efectos son consecuencia conocida de la deshidratación, que es lo que el ACSM busca evitar manteniendo la pérdida por debajo del 2 % del peso.</p>

<h2>El peligro contrario: beber de más</h2>
<p>La hiponatremia asociada al ejercicio puede causar síntomas graves o incluso la muerte. El consenso señala como causa principal consumir más líquido del que se pierde por sudor. Los grupos con mayor riesgo mencionados son las mujeres, las personas mayores y quienes son de menor tamaño, corren despacio, sudan poco y beben mucho. También quienes pierden mucho sodio con el sudor.</p>
<p>Regla práctica: no bebas "por obligación" mucho más de lo que sudas. Si terminas pesando más que al empezar, has bebido de más.</p>

<h2>Consejos rápidos</h2>
<ol>
<li>Pésate antes y después de entrenar para conocer tu sudoración.</li>
<li>Revisa el color de la orina: claro es buena señal; muy oscuro indica que necesitas más líquido.</li>
<li>En sesiones largas o con mucho calor, valora bebidas con sodio.</li>
</ol>
""",
 fuentes=[("ACSM (2007). Posición oficial: Ejercicio y reposición de líquidos (versión en español)","https://infisport.com/mwdownloads/download/link/id/45")])

# ---------------------------------------------------------------- AYUNO 1
art(slug="ayuno-intermitente-que-dice-la-ciencia", cat="Ayuno", img="ayuno-ciencia",
 title="Ayuno intermitente: qué dice realmente la ciencia en 2026",
 desc="Revisamos la evidencia más reciente (Cochrane 2026, BMJ y OCU) sobre el ayuno intermitente: qué sabemos, qué no y qué esperar si lo pruebas.",
 mins=7,
 faq=[("¿El ayuno intermitente adelgaza más que una dieta normal?","Según la revisión Cochrane de 2026, con 22 estudios y 1.995 adultos con sobrepeso u obesidad, el ayuno intermitente podría producir poca o ninguna diferencia de peso frente al asesoramiento dietético tradicional. La certeza de la evidencia es baja o muy baja en la mayoría de resultados."),
      ("¿Hay efectos secundarios?","La revisión Cochrane menciona como posibles efectos el cansancio, los dolores de cabeza y las náuseas, aunque indica que no hay certeza sobre los eventos adversos.")],
 body=f"""
<p class="entradilla">El ayuno intermitente lleva años siendo una de las dietas más buscadas. Pero ¿funciona mejor que comer menos de forma convencional? Esto es lo que dicen las revisiones más sólidas, sin promesas milagro.</p>
<div class="datos3">
<div><strong>22</strong><span>estudios en la revisión Cochrane de 2026</span></div>
<div><strong>99</strong><span>ensayos en el análisis del BMJ</span></div>
<div><strong>≈ 7 kg</strong><span>de pérdida media en los estudios que cita la OCU (3 a 12 meses)</span></div>
</div>
<h2>Qué se entiende por ayuno intermitente</h2>
<p>No existe una definición única. Según el análisis publicado en The BMJ, sus variantes se agrupan en tres grandes categorías: la alimentación con horario restringido (por ejemplo, el 16:8, con 16 horas de ayuno y 8 de comida), el ayuno en días alternos (24 horas de ayuno un día sí y otro no) y el ayuno de día completo (como el 5:2, con cinco días de comida libre y dos de ayuno).</p>
<p>La OCU describe la versión más extendida como pasar al menos 12 horas sin comer, aunque puede llegar a 16 o 20, permitiendo bebidas sin azúcar como agua, café o infusiones.</p>

<h2>La revisión Cochrane de 2026: poca o ninguna diferencia</h2>
<p>La revisión Cochrane, publicada en febrero de 2026, incluyó 22 estudios con 1.995 adultos con sobrepeso u obesidad, con seguimientos de hasta 12 meses. Su conclusión principal: frente al asesoramiento dietético tradicional, el ayuno intermitente podría producir poca o ninguna diferencia en el cambio de peso (21 estudios, 1.430 personas).</p>
<p>Frente a no hacer ninguna intervención, el ayuno probablemente cambia poco el peso, con una confianza moderada. Para el resto de resultados, la confianza es baja o muy baja por métodos poco sólidos y muestras pequeñas. Los autores también señalan que solo se evalúan efectos a corto plazo y que la viabilidad y la sostenibilidad individuales deben pesar en la decisión.</p>

<h2>El análisis del BMJ: similar a la restricción calórica</h2>
<p>Otro trabajo de referencia, una revisión sistemática con metaanálisis en red de 99 ensayos y 6.582 adultos, concluyó que todas las estrategias de ayuno intermitente y de restricción calórica continua reducen el peso frente a comer sin restricciones. Las diferencias entre ayunar y reducir calorías fueron pequeñas. Solo el ayuno en días alternos mostró una ventaja ligera sobre la restricción calórica continua (unos 1,29 kg de diferencia), pero sin alcanzar el umbral de relevancia clínica que fijaron los investigadores.</p>
<p>El mismo trabajo no encontró beneficio sobre el azúcar en sangre ni sobre el colesterol "bueno" en ninguna comparación, y los propios autores piden estudios más largos.</p>

<h2>Lo que sí apunta la OCU</h2>
<p>La OCU recoge estudios en los que se pierden entre 5 y 10 kg en un periodo de 3 a 12 meses, con una media de unos 7 kg, y recuerda que seguir un ayuno o una dieta de restricción calórica convencional no marcaría una gran diferencia. También menciona posibles mejoras en resistencia a la insulina, glucosa, grasa visceral, colesterol LDL y triglicéridos, y recomienda hacerlo con la supervisión de un dietista-nutricionista.</p>
<p>La propia OCU advierte de que el ayuno no está libre de riesgos y de que un estudio observacional presentado en 2024 asoció el ayuno con más muertes cardiovasculares, aunque no estaba publicado y fue criticado metodológicamente. La conclusión honesta es que aún no hay certeza sobre su efecto a largo plazo en el corazón.</p>

<h2>Entonces, ¿merece la pena probarlo?</h2>
<ul>
<li>Si te resulta cómodo y puedes mantenerlo, puede ser una forma de ordenar tus comidas.</li>
<li>Si te genera ansiedad, dolor de cabeza o te hace comer en exceso después, no hay evidencia de que compense.</li>
<li>El mejor plan es el que puedes sostener meses, no el que parece más estricto.</li>
</ul>
<p>Si decides probarlo, mira también <a href="que-comer-al-romper-el-ayuno.html">qué comer al romper el ayuno</a>.</p>
{APP_AYUNO}
""",
 fuentes=[("Cochrane (2026). Ayuno intermitente para el tratamiento del sobrepeso y la obesidad","https://www.cochrane.org/es/node/11572"),
  ("OCU. Ayuno para adelgazar","https://www.ocu.org/alimentacion/adelgazar/informe/ayuno-para-adelgazar"),
  ("Semnani-Azad Z. et al. (2025), The BMJ. Nota de prensa del BMJ Group","https://bmjgroup.com/intermittent-fasting-comparable-to-traditional-diets-for-weight-loss/")])

# ---------------------------------------------------------------- AYUNO 2
art(slug="ayuno-16-8-5-2-dias-alternos-diferencias", cat="Ayuno", img="ayuno-metodos",
 title="Ayuno 16/8, 5:2 y días alternos: diferencias y cuál encaja contigo",
 desc="Comparamos los métodos de ayuno intermitente más conocidos: cómo funcionan, qué dice el BMJ de cada uno y cómo elegir el que puedas mantener.",
 mins=6,
 faq=[("¿Qué es el ayuno 16/8?","Es una forma de alimentación con horario restringido: 16 horas de ayuno y una ventana de 8 horas para comer."),
      ("¿Qué es el ayuno 5:2?","Es un ayuno de día completo: cinco días de comida habitual y dos de ayuno o ingesta muy reducida a la semana."),
      ("¿Qué método es mejor?","El análisis del BMJ vio una ventaja pequeña del ayuno en días alternos, pero sin relevancia clínica clara. Lo más importante es que puedas mantenerlo.")],
 body=f"""
<p class="entradilla">Tres nombres dominan las búsquedas sobre ayuno: 16/8, 5:2 y días alternos. Aquí tienes cómo funciona cada uno, qué sabemos de ellos y cómo decidir sin dejarte llevar por la moda.</p>

<h2>Ayuno 16/8 (alimentación con horario restringido)</h2>
<p>Consiste en concentrar todas las comidas en una ventana de 8 horas y ayunar las otras 16. Durante el ayuno se permiten bebidas sin calorías, como agua, café solo o infusiones. Por ejemplo, comer entre las 12:00 y las 20:00. Existen variantes más suaves, como el 14:10, y más exigentes, como el 18:6 o el 20:4.</p>
<ul>
<li><strong>A favor:</strong> es el más fácil de integrar en la rutina, porque gran parte del ayuno ocurre durmiendo.</li>
<li><strong>En contra:</strong> puede chocar con comidas sociales o con entrenamientos a primera hora.</li>
</ul>

<h2>Ayuno 5:2 (día completo)</h2>
<p>Cinco días a la semana comes de forma habitual y otros dos reduces mucho la ingesta o ayunas. El BMJ lo incluye en la categoría de "ayuno de día completo".</p>
<ul>
<li><strong>A favor:</strong> solo exige disciplina dos días a la semana.</li>
<li><strong>En contra:</strong> los días de ayuno pueden ser duros y es fácil compensar comiendo de más los otros cinco.</li>
</ul>

<h2>Ayuno en días alternos</h2>
<p>Se alternan días de ayuno de 24 horas con días de comida libre. Es el más exigente de los tres.</p>
<p>En el análisis del BMJ (99 ensayos, 6.582 adultos), fue el único que mostró una ventaja pequeña sobre la restricción calórica continua, de unos 1,29 kg. Sin embargo, los propios investigadores indican que ninguna estrategia por sí sola alcanzó un umbral de pérdida de peso clínicamente significativo y que hacen falta estudios más largos.</p>

<h2>Comparativa rápida</h2>
<table>
<thead><tr><th>Método</th><th>Cómo se hace</th><th>Dificultad</th></tr></thead>
<tbody>
<tr><td>14:10</td><td>14 h de ayuno, 10 h para comer</td><td>Baja</td></tr>
<tr><td>16:8</td><td>16 h de ayuno, 8 h para comer</td><td>Baja a media</td></tr>
<tr><td>18:6 y 20:4</td><td>18 o 20 h de ayuno</td><td>Media a alta</td></tr>
<tr><td>5:2</td><td>2 días de ayuno o ingesta muy baja por semana</td><td>Media</td></tr>
<tr><td>Días alternos</td><td>24 h de ayuno cada dos días</td><td>Alta</td></tr>
</tbody></table>
<p class="nota-n">La dificultad es una valoración orientativa nuestra, no un dato de los estudios.</p>

<h2>Cómo elegir</h2>
<ol>
<li>Empieza por el método que menos altere tu vida social y laboral.</li>
<li>Pruébalo dos o tres semanas y observa tu energía, tu sueño y tu apetito.</li>
<li>Si te cuesta, no lo fuerces: la revisión Cochrane de 2026 no encontró ventaja clara frente a una dieta convencional, así que no hay obligación de ayunar.</li>
</ol>
{APP_AYUNO}
""",
 fuentes=[("Semnani-Azad Z. et al. (2025), The BMJ. Nota de prensa del BMJ Group","https://bmjgroup.com/intermittent-fasting-comparable-to-traditional-diets-for-weight-loss/"),
  ("Cochrane (2026). Ayuno intermitente para el tratamiento del sobrepeso y la obesidad","https://www.cochrane.org/es/node/11572"),
  ("OCU. Ayuno para adelgazar","https://www.ocu.org/alimentacion/adelgazar/informe/ayuno-para-adelgazar")])

# ---------------------------------------------------------------- AYUNO 3
art(slug="ayuno-intermitente-riesgos-quien-no-debe-hacerlo", cat="Ayuno", img="ayuno-riesgos",
 title="Ayuno intermitente: beneficios posibles, riesgos y cómo hacerlo con sentido común",
 desc="Qué beneficios cardiometabólicos se han estudiado, qué efectos adversos se mencionan y qué precauciones tomar antes de empezar un ayuno intermitente.",
 mins=6,
 faq=[("¿Qué beneficios se han estudiado?","La OCU menciona menor resistencia a la insulina, glucosa más baja y reducciones de grasa corporal y visceral, colesterol LDL, triglicéridos y proteína C reactiva, aunque con evidencia limitada."),
      ("¿Quién debería consultar antes con un profesional?","Cualquier persona con enfermedades crónicas, que tome medicación, esté embarazada o tenga antecedentes de trastornos de la conducta alimentaria.")],
 body=f"""
<p class="entradilla">Se habla mucho de los beneficios del ayuno, pero poco de sus límites. Aquí separamos lo que se ha observado de lo que aún no se sabe, y por qué conviene tomarlo con calma.</p>

<h2>Beneficios que se han estudiado</h2>
<p>La OCU recoge en su informe posibles mejoras cardiometabólicas: menor resistencia a la insulina, niveles de glucosa más bajos y reducciones de grasa corporal y visceral, de colesterol LDL, triglicéridos y proteína C reactiva. También cita investigaciones según las cuales con ayuno intermitente se perdería una proporción menor de músculo que con una restricción calórica sostenida, y que combinar ayuno y ejercicio podría favorecer una mayor pérdida de peso.</p>
<p>Matiz importante: el ejercicio en ayunas no quemaría más grasa por sí mismo, según el mismo informe.</p>

<h2>Lo que la evidencia no confirma</h2>
<p>La revisión Cochrane de 2026 considera que, para la mayoría de los resultados, la certeza de la evidencia es baja o muy baja. Ningún estudio incluido informó sobre el control de la diabetes ni sobre medidas globales de otras enfermedades asociadas, y los seguimientos llegan como máximo a 12 meses.</p>
<p>El análisis del BMJ, por su parte, no encontró beneficio sobre el azúcar en sangre ni sobre el colesterol "bueno" en ninguna comparación de estrategias.</p>

<h2>Riesgos y efectos adversos</h2>
<ul>
<li>Cochrane menciona como posibles efectos perjudiciales el cansancio, los dolores de cabeza y las náuseas, aunque indica que no hay certeza sobre los eventos adversos.</li>
<li>El BMJ señaló que la alimentación con horario restringido supuso un pequeño aumento del colesterol total y del LDL frente al ayuno de día completo.</li>
<li>La OCU recuerda que no hay certeza sobre los efectos en la mortalidad cardíaca y comenta un estudio observacional de 2024 que asoció el ayuno con más muertes cardiovasculares, con serias críticas metodológicas.</li>
</ul>

<h2>Cuándo consultar antes con un profesional</h2>
<p>Ninguna de las fuentes consultadas da una lista cerrada de contraindicaciones, y la OCU solo recomienda hacerlo bajo supervisión de un dietista-nutricionista. Por prudencia, consulta antes si:</p>
<ul>
<li>Tienes diabetes u otra enfermedad crónica, o tomas medicación que dependa de las comidas.</li>
<li>Estás embarazada o en lactancia.</li>
<li>Has tenido o tienes un trastorno de la conducta alimentaria.</li>
<li>Eres menor de edad o una persona mayor frágil.</li>
</ul>

<h2>Cómo hacerlo con sentido común</h2>
<ol>
<li>Empieza con un ayuno suave (por ejemplo, 12 o 14 horas) y alarga solo si te sientes bien.</li>
<li>Bebe agua, café solo o infusiones sin azúcar durante el ayuno.</li>
<li>Cuando comas, prioriza proteína, verdura, legumbres y fruta en lugar de compensar con ultraprocesados.</li>
<li>Para si notas mareo intenso, malestar persistente o pensamientos obsesivos con la comida.</li>
</ol>
{APP_AYUNO}
""",
 fuentes=[("OCU. Ayuno para adelgazar","https://www.ocu.org/alimentacion/adelgazar/informe/ayuno-para-adelgazar"),
  ("Cochrane (2026). Ayuno intermitente para el tratamiento del sobrepeso y la obesidad","https://www.cochrane.org/es/node/11572"),
  ("Semnani-Azad Z. et al. (2025), The BMJ. Resumen en HealthDay","https://www.healthday.com/healthpro-news/weight-loss/intermittent-fasting-reduces-body-weight-versus-ad-libitum-diet")])

# ================================================================ PLANTILLAS
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'
def head(title, desc, canon, img, tipo, extra):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="icon" href="../assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="../assets/pombo-icon.png">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{DOM}/assets/blog/{img}.jpg">
<meta property="og:type" content="{tipo}">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
{extra}
<link rel="stylesheet" href="../assets/site.css">
</head>
<body>
<a class="pular" href="#conteudo">Saltar al contenido</a>
<header class="topo"><div class="faixa">
<a href="../index.html" class="marca" aria-label="Pombo AI, inicio"><img src="../assets/pombo-icon.png" alt="" width="36" height="36"><span>Pombo AI</span></a>
<nav aria-label="Menú principal"><ul>
<li><a href="../index.html#faq">Preguntas frecuentes</a></li><li><a href="index.html" aria-current="page">Blog</a></li><li><a href="../imprensa.html">Prensa</a></li>
</ul></nav></div></header>
"""
FOOT = """<footer class="pie-blog"><div class="faixa">
<p>© 2026 Pombo AI · <a href="../politica-de-privacidade.html">Privacidad</a> · <a href="../termos-de-uso.html">Términos</a> · <a href="../politica-de-cookies.html">Cookies</a></p>
<p>Fotos: <a href="https://unsplash.com/license" rel="noopener" target="_blank">Unsplash</a>. Datos nutricionales: USDA FoodData Central.</p>
</div></footer>
</body></html>
"""
CAT_CLASE = {"Ayuno": "c-ayuno", "Recetas": "c-recetas", "Hidratación": "c-hidra", "Pescado": "c-pescado"}
AUTOR = "Equipo editorial de Pombo AI"

os.makedirs(ROOT + "/blog", exist_ok=True)
for f in os.listdir(ROOT + "/blog"):
    if f.endswith(".html"): os.remove(ROOT + "/blog/" + f)

def tarjeta(b, grande=False):
    clase = "tarjeta destacada" if grande else "tarjeta"
    sz = "" if grande else "-p"
    return (f'<article class="{clase}" data-cat="{b["cat"]}"><a class="tarjeta-img" href="{b["slug"]}.html" tabindex="-1" aria-hidden="true"><img src="../assets/blog/{b["img"]}{sz}.jpg" alt="" width="{1200 if grande else 640}" height="{900 if grande else 480}" loading="{"eager" if grande else "lazy"}"></a>'
            f'<div class="tarjeta-txt"><span class="cat {CAT_CLASE[b["cat"]]}">{b["cat"]}</span><h2><a href="{b["slug"]}.html">{E(b["title"])}</a></h2>'
            + (f'<p>{E(b["desc"])}</p>' if grande else '') +
            f'<p class="meta">{FECHA_TXT} · {b["mins"]} min de lectura</p></div></article>')

for a in A:
    url = f"{DOM}/blog/{a['slug']}.html"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "headline": a["title"], "description": a["desc"], "inLanguage": "es-ES", "datePublished": FECHA, "dateModified": FECHA,
         "mainEntityOfPage": url, "image": f"{DOM}/assets/blog/{a['img']}.jpg", "author": {"@type": "Organization", "name": AUTOR},
         "publisher": {"@type": "Organization", "name": "Pombo AI", "logo": {"@type": "ImageObject", "url": DOM + "/assets/pombo-icon.png"}}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": DOM + "/"}, {"@type": "ListItem", "position": 2, "name": "Blog", "item": DOM + "/blog/"}, {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in a["faq"]]}]}
    recs = [r for r in (BAC if a["slug"].startswith("recetas-de-bacalao") else ADE if "adelgazar" in a["slug"] else MUS if "masa-muscular" in a["slug"] else [])]
    for r in recs:
        n = nutr(r["ing"], r["rac"])
        ld["@graph"].append({"@type": "Recipe", "name": r["t"], "image": f"{DOM}/assets/blog/{r['img']}.jpg", "author": {"@type": "Organization", "name": AUTOR},
            "recipeYield": f"{r['rac']} raciones", "totalTime": f"PT{r['min']}M", "recipeIngredient": [t for t, _, _ in r["ing"]],
            "recipeInstructions": [{"@type": "HowToStep", "text": s} for s in r["pasos"]],
            "nutrition": {"@type": "NutritionInformation", "calories": f"{n[0]:.0f} kcal", "proteinContent": f"{n[1]:.0f} g", "carbohydrateContent": f"{n[2]:.0f} g", "fatContent": f"{n[3]:.0f} g", "fiberContent": f"{n[4]:.0f} g"}})
    extra = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace("</", "<\\/") + '</script>'
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(r)}</p></details>" for q, r in a["faq"])
    fu = "<h2>Fuentes</h2><ul class=\"fuentes\">" + "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{E(t)}</a></li>' for t, u in a["fuentes"]) + "</ul>"
    rel = [b for b in A if b is not a and b["cat"] == a["cat"]][:3]
    rel += [b for b in A if b is not a and b not in rel][:3 - len(rel)]
    doc = head(a["title"] + " | Pombo AI", a["desc"], url, a["img"], "article", extra) + f"""
<main id="conteudo" class="articulo">
<header class="art-cabeza"><div class="faixa estrecha">
<p class="migas"><a href="../index.html">Inicio</a> › <a href="index.html">Blog</a> › {a['cat']}</p>
<span class="cat {CAT_CLASE[a['cat']]}">{a['cat']}</span>
<h1>{E(a['title'])}</h1>
<p class="art-meta"><img src="../assets/pombo-icon.png" alt="" width="32" height="32"><span>Por el equipo editorial de Pombo AI<br>{FECHA_TXT} · {a['mins']} min de lectura</span></p>
</div>
<figure class="art-portada faixa"><img src="../assets/blog/{a['img']}.jpg" alt="{E(a['title'])}" width="1200" height="900"><figcaption>Foto: Unsplash</figcaption></figure>
</header>
<div class="faixa estrecha cuerpo legal">
{a['body']}
<h2>Preguntas frecuentes</h2>
<div class="faq-art">{faq}</div>
{fu}
<div class="aviso"><p><strong>Aviso:</strong> {AV_SALUD}</p></div>
</div>
<section class="relacionados"><div class="faixa"><h2>Sigue leyendo</h2><div class="rejilla">{''.join(tarjeta(b) for b in rel)}</div></div></section>
</main>
""" + FOOT
    open(f"{ROOT}/blog/{a['slug']}.html", "w").write(doc)

cats = ["Todos"] + sorted({a["cat"] for a in A})
chips = "".join(f'<button type="button" class="chip{" activo" if c=="Todos" else ""}" data-f="{c}">{c}</button>' for c in cats)
ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Blog de Pombo AI", "description": "Artículos sobre ayuno, hidratación, pescado y recetas saludables.", "inLanguage": "es-ES", "url": DOM + "/blog/",
      "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{DOM}/blog/{a['slug']}.html", "image": f"{DOM}/assets/blog/{a['img']}.jpg", "datePublished": FECHA} for a in A]}
idx = head("Blog de nutrición: recetas, ayuno, pescado e hidratación | Pombo AI",
           "Recetas con información nutricional, ayuno intermitente, pescado e hidratación en el deporte. Artículos claros, con fuentes y sin promesas milagro.",
           DOM + "/blog/", A[0]["img"], "website", '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>') + f"""
<main id="conteudo" class="blog-portada">
<section class="blog-cabeza"><div class="faixa">
<p class="antetitulo">Blog de Pombo AI</p>
<h1>Come mejor, sin complicarte</h1>
<p class="guia">Recetas con su información nutricional, ayuno intermitente, pescado e hidratación explicados con fuentes y sin promesas milagro.</p>
</div></section>
<div class="faixa">
{tarjeta(A[0], True)}
<div class="filtros" role="group" aria-label="Filtrar por categoría">{chips}</div>
<div class="rejilla" id="rejilla">{''.join(tarjeta(b) for b in A[1:])}</div>
</div>
</main>
<script>
document.querySelectorAll('.chip').forEach(function(c){{c.addEventListener('click',function(){{
 document.querySelectorAll('.chip').forEach(function(x){{x.classList.toggle('activo',x===c)}});
 var f=c.dataset.f; document.querySelectorAll('#rejilla .tarjeta').forEach(function(t){{t.hidden=!(f==='Todos'||t.dataset.cat===f)}});
}})}});
</script>
""" + FOOT
open(ROOT + "/blog/index.html", "w").write(idx)

sm = open(ROOT + "/sitemap.xml").read()
sm = re.sub(r'\s*<url>\s*<loc>[^<]*/blog/[^<]*</loc>.*?</url>', '', sm, flags=re.S)
urls = f'  <url><loc>{DOM}/blog/</loc><lastmod>{FECHA}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
for a in A:
    urls += f'  <url><loc>{DOM}/blog/{a["slug"]}.html</loc><lastmod>{FECHA}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority><image:image xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"><image:loc>{DOM}/assets/blog/{a["img"]}.jpg</image:loc></image:image></url>\n'
sm = sm.replace("</urlset>", urls + "</urlset>")
open(ROOT + "/sitemap.xml", "w").write(sm)

for x in (ADE + MUS + BAC):
    n = nutr(x["ing"], x["rac"]); print(f'{x["t"][:42]:44} {n[0]:5.0f} kcal P{n[1]:4.0f} H{n[2]:4.0f} G{n[3]:4.0f} F{n[4]:4.0f}', sellos(n))
print(len(A), "artículos")
