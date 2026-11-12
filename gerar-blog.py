import os, json, html
ROOT="/home/claude/pagina-pombo-ai-"
DOM="https://www.SEU-DOMINIO.com.br"
FECHA="2026-11-12"; FECHA_TXT="12 de noviembre de 2026"
AV_SALUD="Este artículo es informativo y no sustituye el consejo de un médico o dietista-nutricionista. Si tienes una enfermedad, tomas medicación, estás embarazada o has tenido un trastorno de la conducta alimentaria, consulta con un profesional antes de cambiar tu alimentación."
CTA=('<div class="aviso cta"><p><strong>¿Quieres saber cuánto comes de verdad?</strong> Con Pombo AI haces una foto a tu plato y la inteligencia artificial estima calorías y macros en segundos. Es una estimación orientativa, no un dato médico.</p><p><a href="/">Conoce Pombo AI</a></p></div>')

A=[]
def art(**k): A.append(k)

art(slug="ayuno-intermitente-que-dice-la-ciencia", cat="Ayuno",
 title="Ayuno intermitente: qué dice realmente la ciencia en 2026",
 desc="Revisamos la evidencia más reciente (Cochrane 2026, BMJ y OCU) sobre el ayuno intermitente: qué sabemos, qué no y qué esperar si lo pruebas.",
 mins=7,
 faq=[("¿El ayuno intermitente adelgaza más que una dieta normal?","Según la revisión Cochrane de 2026, con 22 estudios y 1.995 adultos con sobrepeso u obesidad, el ayuno intermitente podría producir poca o ninguna diferencia de peso frente al asesoramiento dietético tradicional. La certeza de la evidencia es baja o muy baja en la mayoría de resultados."),
      ("¿Hay efectos secundarios?","La revisión Cochrane menciona como posibles efectos el cansancio, los dolores de cabeza y las náuseas, aunque indica que no hay certeza sobre los eventos adversos.")],
 body="""
<p class="entradilla">El ayuno intermitente lleva años siendo una de las dietas más buscadas. Pero ¿funciona mejor que comer menos de forma convencional? Esto es lo que dicen las revisiones más sólidas, sin promesas milagro.</p>

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
<p>Sea cual sea tu método, saber cuánto comes marca la diferencia. Puedes registrar tus comidas con una foto y comparar días de ayuno y días normales.</p>
""",
 fuentes=[("Cochrane (2026). Ayuno intermitente para el tratamiento del sobrepeso y la obesidad","https://www.cochrane.org/es/node/11572"),
  ("OCU. Ayuno para adelgazar","https://www.ocu.org/alimentacion/adelgazar/informe/ayuno-para-adelgazar"),
  ("Semnani-Azad Z. et al. (2025), The BMJ. Intermittent fasting y restricción calórica: revisión sistemática y metaanálisis en red","https://bmjgroup.com/intermittent-fasting-comparable-to-traditional-diets-for-weight-loss/")])

art(slug="ayuno-16-8-5-2-dias-alternos-diferencias", cat="Ayuno",
 title="Ayuno 16/8, 5:2 y días alternos: diferencias y cuál encaja contigo",
 desc="Comparamos los tres métodos de ayuno intermitente más conocidos: cómo funcionan, qué dice el BMJ de cada uno y cómo elegir el que puedas mantener.",
 mins=6,
 faq=[("¿Qué es el ayuno 16/8?","Es una forma de alimentación con horario restringido: 16 horas de ayuno y una ventana de 8 horas para comer."),
      ("¿Qué es el ayuno 5:2?","Es un ayuno de día completo: cinco días de comida habitual y dos de ayuno o ingesta muy reducida a la semana."),
      ("¿Qué método es mejor?","El análisis del BMJ vio una ventaja pequeña del ayuno en días alternos, pero sin relevancia clínica clara. Lo más importante es que puedas mantenerlo.")],
 body="""
<p class="entradilla">Tres nombres dominan las búsquedas sobre ayuno: 16/8, 5:2 y días alternos. Aquí tienes cómo funciona cada uno, qué sabemos de ellos y cómo decidir sin dejarte llevar por la moda.</p>

<h2>Ayuno 16/8 (alimentación con horario restringido)</h2>
<p>Consiste en concentrar todas las comidas en una ventana de 8 horas y ayunar las otras 16. Durante el ayuno se permiten bebidas sin calorías, como agua, café solo o infusiones. Por ejemplo, comer entre las 12:00 y las 20:00.</p>
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
<tr><td>16/8</td><td>16 h de ayuno, 8 h para comer</td><td>Baja a media</td></tr>
<tr><td>5:2</td><td>2 días de ayuno o ingesta muy baja por semana</td><td>Media</td></tr>
<tr><td>Días alternos</td><td>24 h de ayuno cada dos días</td><td>Alta</td></tr>
</tbody></table>
<p>La dificultad es una valoración orientativa nuestra, no un dato de los estudios.</p>

<h2>Cómo elegir</h2>
<ol>
<li>Empieza por el método que menos altere tu vida social y laboral.</li>
<li>Pruébalo dos o tres semanas y observa tu energía, tu sueño y tu apetito.</li>
<li>Si te cuesta, no lo fuerces: la revisión Cochrane de 2026 no encontró ventaja clara frente a una dieta convencional, así que no hay obligación de ayunar.</li>
</ol>
<p>Durante la prueba, registra qué comes en tu ventana de alimentación. Muchas personas descubren que comen más rápido o peor cuando rompen el ayuno.</p>
""",
 fuentes=[("Semnani-Azad Z. et al. (2025), The BMJ. Nota de prensa del BMJ Group","https://bmjgroup.com/intermittent-fasting-comparable-to-traditional-diets-for-weight-loss/"),
  ("Cochrane (2026). Ayuno intermitente para el tratamiento del sobrepeso y la obesidad","https://www.cochrane.org/es/node/11572"),
  ("OCU. Ayuno para adelgazar","https://www.ocu.org/alimentacion/adelgazar/informe/ayuno-para-adelgazar")])

art(slug="ayuno-intermitente-riesgos-quien-no-debe-hacerlo", cat="Ayuno",
 title="Ayuno intermitente: beneficios posibles, riesgos y cómo hacerlo con sentido común",
 desc="Qué beneficios cardiometabólicos se han estudiado, qué efectos adversos se mencionan y qué precauciones tomar antes de empezar un ayuno intermitente.",
 mins=6,
 faq=[("¿Qué beneficios se han estudiado?","La OCU menciona menor resistencia a la insulina, glucosa más baja y reducciones de grasa corporal y visceral, colesterol LDL, triglicéridos y proteína C reactiva, aunque con evidencia limitada."),
      ("¿Quién debería consultar antes con un profesional?","Cualquier persona con enfermedades crónicas, que tome medicación, esté embarazada o tenga antecedentes de trastornos de la conducta alimentaria.")],
 body="""
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
<li>Empieza con un ayuno suave (por ejemplo, 12 horas) y alarga solo si te sientes bien.</li>
<li>Bebe agua, café solo o infusiones sin azúcar durante el ayuno.</li>
<li>Cuando comas, prioriza proteína, verdura, legumbres y fruta en lugar de compensar con ultraprocesados.</li>
<li>Para si notas mareo intenso, malestar persistente o pensamientos obsesivos con la comida.</li>
</ol>
""",
 fuentes=[("OCU. Ayuno para adelgazar","https://www.ocu.org/alimentacion/adelgazar/informe/ayuno-para-adelgazar"),
  ("Cochrane (2026). Ayuno intermitente para el tratamiento del sobrepeso y la obesidad","https://www.cochrane.org/es/node/11572"),
  ("Semnani-Azad Z. et al. (2025), The BMJ. Resumen en HealthDay","https://www.healthday.com/healthpro-news/weight-loss/intermittent-fasting-reduces-body-weight-versus-ad-libitum-diet")])

art(slug="hidratacion-ejercicio-cuanta-agua-beber", cat="Hidratación",
 title="Hidratación y ejercicio: cuánta agua beber antes, durante y después",
 desc="Guía práctica basada en el consenso del American College of Sports Medicine: pérdida de peso por sudor, cantidades orientativas y riesgos de beber de menos o de más.",
 mins=7,
 faq=[("¿Cuánta agua beber antes de entrenar?","El ACSM sugiere beber despacio unos 5 a 7 mL por kilo de peso corporal al menos 4 horas antes del ejercicio. Si no orinas o la orina es muy oscura, añadir 3 a 5 mL/kg unas 2 horas antes."),
      ("¿Puedo beber demasiado agua haciendo deporte?","Sí. Beber más de lo que sudas puede causar hiponatremia asociada al ejercicio, una bajada de sodio en sangre que puede ser grave."),
      ("¿Cuánto beber después de entrenar?","Para una recuperación rápida tras una deshidratación importante, el ACSM sugiere beber alrededor de 1,5 litros por cada kilo de peso perdido.")],
 body="""
<p class="entradilla">Beber poco al hacer ejercicio perjudica el rendimiento y la salud, pero beber de más también tiene riesgos. Estas son las pautas del American College of Sports Medicine (ACSM) explicadas en claro.</p>

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

art(slug="recetas-saludables-para-adelgazar-sobrepeso", cat="Recetas",
 title="5 recetas saludables y saciantes para perder peso sin pasar hambre",
 desc="Cinco recetas fáciles con mucha verdura, legumbres y proteína para ayudarte a comer mejor si tienes sobrepeso. Con consejos para medir raciones.",
 mins=8,
 faq=[("¿Qué debe tener una comida para saciar?","Combinar proteína (huevo, pescado, legumbres, pollo), fibra (verdura, legumbres, integrales) y una grasa saludable en cantidad moderada ayuda a sentirse lleno con menos calorías.")],
 body="""
<p class="entradilla">Perder peso no pasa por comer poco, sino por comer bien: platos con mucha verdura, proteína y fibra que sacian. Estas cinco recetas son sencillas, económicas y fáciles de repetir.</p>
<div class="aviso"><p>Las calorías exactas dependen de las marcas y cantidades. Por eso no ponemos cifras cerradas: pesa los ingredientes o haz una foto al plato con Pombo AI para obtener una estimación. Si tienes obesidad o una enfermedad, consulta con tu médico o dietista.</p></div>

<h2>1. Ensalada templada de garbanzos con atún y pimiento</h2>
<p><strong>Para 2 personas · 15 minutos</strong></p>
<ul><li>1 bote de garbanzos cocidos, escurridos y enjuagados</li><li>2 latas de atún al natural</li><li>1 pimiento rojo asado en tiras</li><li>½ cebolla roja en juliana fina</li><li>Perejil, zumo de limón, 1 cucharada de aceite de oliva virgen extra, sal y pimienta</li></ul>
<p>Calienta los garbanzos 2 minutos en un cazo con un poco de agua, escúrrelos y mézclalos con el resto. Aliña con limón y el aceite. Los garbanzos aportan fibra y proteína vegetal, y el atún, proteína magra.</p>

<h2>2. Tortilla de claras y verduras al horno</h2>
<p><strong>Para 2 personas · 25 minutos</strong></p>
<ul><li>2 huevos enteros y 4 claras</li><li>1 calabacín y 1 puñado de espinacas</li><li>½ cebolla</li><li>Especias al gusto, sal y un chorrito de aceite</li></ul>
<p>Sofríe la cebolla y el calabacín con poco aceite hasta que estén tiernos y añade las espinacas. Bate los huevos con las claras, mezcla y vierte en un molde. Hornea a 180 °C unos 15 minutos hasta que cuaje. Rinde mucho volumen con poca energía.</p>

<h2>3. Crema de calabacín y puerro con yogur</h2>
<p><strong>Para 3 personas · 25 minutos</strong></p>
<ul><li>3 calabacines y 2 puerros</li><li>1 patata pequeña</li><li>Caldo de verduras sin sal añadida</li><li>1 yogur natural sin azúcar para servir</li></ul>
<p>Cuece las verduras en el caldo 15 minutos, tritura, añade sal al gusto y sirve con una cucharada de yogur. Una buena primera opción para empezar la comida con algo caliente que llena.</p>

<h2>4. Pollo al limón con verduras asadas</h2>
<p><strong>Para 2 personas · 35 minutos</strong></p>
<ul><li>2 pechugas de pollo</li><li>1 limón (zumo y ralladura)</li><li>Brócoli, zanahoria y cebolla en trozos</li><li>1 cucharada de aceite de oliva, ajo, tomillo y sal</li></ul>
<p>Marina el pollo con limón, ajo y tomillo 10 minutos. Coloca todo en una bandeja con las verduras y el aceite y hornea a 200 °C durante 25 minutos, dándole la vuelta a mitad de cocción.</p>

<h2>5. Lentejas estofadas con verduras</h2>
<p><strong>Para 4 personas · 40 minutos</strong></p>
<ul><li>300 g de lentejas pardinas</li><li>1 zanahoria, 1 pimiento y 1 tomate</li><li>1 cebolla y 2 dientes de ajo</li><li>Pimentón, laurel y sal</li></ul>
<p>Sofríe las verduras, añade las lentejas, el pimentón y agua que las cubra por dos dedos. Cuece 30 minutos a fuego suave. Sin chorizo ni panceta, quedan igual de sabrosas y mucho más ligeras.</p>

<h2>Trucos para que funcione</h2>
<ol>
<li>Llena la mitad del plato de verdura.</li>
<li>Incluye una fuente de proteína en cada comida.</li>
<li>Sirve en plato llano, no en fuente, y repite solo si sigues con hambre.</li>
<li>Bebe agua y deja los refrescos para ocasiones puntuales.</li>
</ol>
"""+CTA, fuentes=[])

art(slug="recetas-para-ganar-masa-muscular-proteina", cat="Recetas",
 title="Recetas para ganar masa muscular: cuánta proteína necesitas y 5 platos fáciles",
 desc="Qué dice la ciencia sobre la proteína para ganar músculo (alrededor de 1,6 g/kg al día) y cinco recetas ricas en proteína y energía para entrenar mejor.",
 mins=8,
 faq=[("¿Cuánta proteína necesito para ganar músculo?","Un metaanálisis publicado en el British Journal of Sports Medicine con 49 estudios y 1.863 participantes indica que, con suplementación proteica, ingestas superiores a unos 1,6 g/kg al día no aportan más ganancia de masa libre de grasa en entrenamiento de fuerza."),
      ("¿Es imprescindible tomar batidos de proteína?","No. Los batidos son una forma cómoda de llegar a tu cantidad, pero se puede lograr con alimentos como huevos, legumbres, pescado, carne magra y lácteos.")],
 body="""
<p class="entradilla">Para ganar músculo hacen falta tres cosas: entrenamiento de fuerza, suficiente proteína y energía para sostenerlo. Aquí tienes qué dice la investigación y cinco recetas para llevarlo a tu plato.</p>

<h2>Cuánta proteína necesitas</h2>
<p>Un metaanálisis con metarregresión publicado en el British Journal of Sports Medicine (Morton y colaboradores, 2018) analizó 49 estudios con 1.863 participantes. Concluyó que la suplementación con proteína aumenta de forma significativa la fuerza y el tamaño muscular durante el entrenamiento de fuerza, y que con suplementación las ingestas superiores a unos 1,6 g de proteína por kilo de peso y día no aportan ganancias adicionales de masa libre de grasa.</p>
<p>Para una persona de 75 kg, eso son unos 120 g de proteína al día. Los autores también señalan que el entrenamiento de fuerza es un estímulo mucho más potente que añadir proteína, y que la eficacia de la suplementación disminuye con la edad y aumenta con la experiencia en el entrenamiento.</p>
<div class="aviso"><p>Las personas con enfermedad renal u otras patologías deben consultar con su médico antes de aumentar la proteína. Las cantidades de las recetas son orientativas; usa Pombo AI para medir lo que realmente comes.</p></div>

<h2>1. Bowl de arroz, pollo y aguacate</h2>
<p><strong>1 persona · 20 minutos</strong></p>
<ul><li>150 g de pechuga de pollo a la plancha</li><li>Arroz cocido (una taza)</li><li>½ aguacate, maíz y tomate cherry</li><li>Limón, sal y un chorrito de aceite</li></ul>
<p>Combina todo en un bol. Aporta proteína, hidratos para entrenar y grasas saludables.</p>

<h2>2. Revuelto de huevos con atún y espinacas sobre tostada integral</h2>
<p><strong>1 persona · 10 minutos</strong></p>
<ul><li>3 huevos</li><li>1 lata de atún al natural</li><li>Un puñado de espinacas</li><li>2 rebanadas de pan integral</li></ul>
<p>Saltea las espinacas, añade los huevos batidos y el atún y remueve hasta cuajar. Sirve sobre las tostadas. Un desayuno o cena rápidos y completos.</p>

<h2>3. Lentejas con arroz y huevo duro</h2>
<p><strong>2 personas · 35 minutos</strong></p>
<ul><li>200 g de lentejas</li><li>100 g de arroz</li><li>2 huevos cocidos</li><li>Zanahoria, cebolla y pimentón</li></ul>
<p>Cuece las lentejas con las verduras, añade el arroz los últimos 15 minutos y sirve con el huevo troceado. Combina legumbre y cereal para una comida muy completa y económica.</p>

<h2>4. Salmón al horno con patata y brócoli</h2>
<p><strong>2 personas · 35 minutos</strong></p>
<ul><li>2 lomos de salmón</li><li>2 patatas medianas en rodajas</li><li>1 brócoli en ramilletes</li><li>Aceite, limón, eneldo y sal</li></ul>
<p>Hornea las patatas 15 minutos a 200 °C, añade el brócoli y el salmón y continúa 12 a 15 minutos más. Buena fuente de proteína y grasas del pescado.</p>

<h2>5. Batido de plátano, avena y yogur</h2>
<p><strong>1 persona · 5 minutos</strong></p>
<ul><li>1 plátano</li><li>40 g de copos de avena</li><li>1 yogur griego natural</li><li>200 mL de leche (o bebida vegetal)</li><li>Canela</li></ul>
<p>Tritura todo. Ideal después de entrenar o como merienda para sumar proteína y energía sin cocinar.</p>

<h2>Consejos para comer más proteína sin complicarte</h2>
<ol>
<li>Reparte la proteína en 3 o 4 comidas del día.</li>
<li>Mezcla fuentes animales y vegetales: huevos, pescado, lácteos, legumbres, frutos secos.</li>
<li>Come en superávit moderado de energía: sin sobrante calórico es difícil ganar masa.</li>
<li>Duerme bien y mantén una progresión en tus entrenamientos.</li>
</ol>
"""+CTA, fuentes=[("Morton R.W. et al. (2018), British Journal of Sports Medicine, 52(6):376-384. PubMed","https://pubmed.ncbi.nlm.nih.gov/28698222/"),
  ("Resumen del estudio de Morton et al. en NutritionInsight","https://www.nutritioninsight.com/news/the-debate-is-over-protein-supplements-significantly-benefit-muscle-mass.html")])

HEAD=lambda title,desc,canon,extra,css="../assets/site.css": f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="icon" href="../assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="../assets/pombo-icon.png">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{DOM}/assets/pombo-icon.png">
<meta property="og:type" content="article">
<meta property="og:locale" content="es_ES">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{extra}
<link rel="stylesheet" href="{css}">
</head>
<body>
<a class="pular" href="#conteudo">Saltar al contenido</a>
<header class="topo"><div class="faixa">
<a href="/" class="marca" aria-label="Pombo AI, inicio"><img src="../assets/pombo-icon.png" alt="" width="36" height="36"><span>Pombo AI</span></a>
<nav aria-label="Menú principal"><ul>
<li><a href="/#faq">Preguntas frecuentes</a></li><li><a href="/blog/">Blog</a></li><li><a href="/imprensa.html">Prensa</a></li>
</ul></nav></div></header>
"""
FOOT="""<footer><div class="faixa"><p class="direitos" style="margin-top:0;border-top:0;padding-top:0;text-align:center;">© 2026 Pombo AI. Todos los derechos reservados. · <a href="/politica-de-privacidade.html">Privacidad</a> · <a href="/termos-de-uso.html">Términos</a></p></div></footer>
</body></html>
"""
os.makedirs(ROOT+"/blog",exist_ok=True)
for a in A:
    url=f"{DOM}/blog/{a['slug']}.html"
    ld={"@context":"https://schema.org","@graph":[
      {"@type":"BlogPosting","headline":a["title"],"description":a["desc"],"inLanguage":"es-ES","datePublished":FECHA,"dateModified":FECHA,
       "mainEntityOfPage":url,"author":{"@type":"Organization","name":"Equipo editorial de Pombo AI"},
       "publisher":{"@type":"Organization","name":"Pombo AI","logo":{"@type":"ImageObject","url":DOM+"/assets/pombo-icon.png"}},
       "image":DOM+"/assets/pombo-icon.png"},
      {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":DOM+"/"},{"@type":"ListItem","position":2,"name":"Blog","item":DOM+"/blog/"},{"@type":"ListItem","position":3,"name":a["title"],"item":url}]}]}
    if a["faq"]:
        ld["@graph"].append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":r}} for q,r in a["faq"]]})
    extra='<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>'
    faq="".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(r)}</p>" for q,r in a["faq"])
    fu=("<h2>Fuentes</h2><ul>"+"".join(f'<li><a href="{u}" rel="noopener" target="_blank">{html.escape(t)}</a></li>' for t,u in a["fuentes"])+"</ul>") if a["fuentes"] else ""
    rel="".join(f'<li><a href="/blog/{b["slug"]}.html">{html.escape(b["title"])}</a></li>' for b in A if b is not a)
    doc=HEAD(a["title"]+" | Pombo AI",a["desc"],url,extra)+f"""
<main id="conteudo" class="legal articulo"><div class="faixa">
<p class="migas"><a href="/">Inicio</a> › <a href="/blog/">Blog</a> › {a['cat']}</p>
<h1>{html.escape(a['title'])}</h1>
<p class="atualizado">Por el equipo editorial de Pombo AI · Publicado el {FECHA_TXT} · {a['mins']} min de lectura</p>
{a['body']}
<h2>Preguntas frecuentes</h2>
{faq}
{fu}
<div class="aviso"><p><strong>Aviso:</strong> {AV_SALUD}</p></div>
<h2>Sigue leyendo</h2><ul>{rel}</ul>
<a class="voltar" href="/blog/">← Volver al blog</a>
</div></main>
"""+FOOT
    open(f"{ROOT}/blog/{a['slug']}.html","w").write(doc)

cards="".join(f'<li class="tarjeta-blog"><span class="cat">{a["cat"]}</span><h2><a href="/blog/{a["slug"]}.html">{html.escape(a["title"])}</a></h2><p>{html.escape(a["desc"])}</p><span class="meta">{a["mins"]} min de lectura</span></li>' for a in A)
ld={"@context":"https://schema.org","@type":"Blog","name":"Blog de Pombo AI","description":"Artículos sobre alimentación, ayuno, hidratación y recetas saludables.","inLanguage":"es-ES","url":DOM+"/blog/"}
idx=HEAD("Blog de nutrición, ayuno, hidratación y recetas | Pombo AI","Artículos claros y con fuentes sobre ayuno intermitente, hidratación en el ejercicio y recetas para adelgazar o ganar masa muscular.",DOM+"/blog/",'<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>').replace('og:type" content="article"','og:type" content="website"')+f"""
<main id="conteudo" class="blog-indice"><div class="faixa">
<h1>Blog de Pombo AI</h1>
<p class="guia">Alimentación, ayuno, hidratación y recetas explicados con fuentes y sin promesas milagro.</p>
<ul class="rejilla-blog">{cards}</ul>
</div></main>
"""+FOOT
open(ROOT+"/blog/index.html","w").write(idx)

# sitemap
sm=open(ROOT+"/sitemap.xml").read()
import re
sm=re.sub(r'\s*<url>\s*<loc>[^<]*/blog[^<]*</loc>.*?</url>','',sm,flags=re.S)
urls=f'  <url><loc>{DOM}/blog/</loc><lastmod>{FECHA}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
for a in A: urls+=f'  <url><loc>{DOM}/blog/{a["slug"]}.html</loc><lastmod>{FECHA}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'
sm=sm.replace("</urlset>",urls+"</urlset>")
open(ROOT+"/sitemap.xml","w").write(sm)
print(len(A))
