
"""
HE HECHO UN PROGRAMA QUE FUNCIONA COMO UN CALCULADOR DE LA RUTA MÁS CERCANA ENTRE DOS PUNTOS DE UNA CIUDAD DADOS POR EL USUARIO.
ADEMÁS IMPRIME EL MAPA DE LA CIUDAD Y EL MAPA DE LA CIUDAD CON LA RUTA DIBUJADA. POR ÚLTIMO, TAMBIÉN PROPORCIONA LA DISTANCIA A RECORRER ENTRE 
LOS DOS PUNTOS SEGÚN LA RUTA PROPORCIONADA
"""

#Importamos las bibliotecas necesarias
import osmnx as ox
from geopy.geocoders import Nominatim



#Inicializamos la API Nominatim
geolocator= Nominatim(user_agent="calculador_rutas_Grich")

try:
    #Le pedimos el nombre de la ciudad y del país al usuario 
    ciudad=input("Introduce el nombre de la ciudad y del pais (ciudad, pais(en inglés)):")

except ox._errors.InsufficientResponseError:
    print("ERROR: Ciudad no encontrada")

#Le preguntamos al usuario cuál es el tipo de vía con la cual dibujar el mapa
print(" ----- ELIGE EL TIPO DE VÍA ----- \n  \n       1.Cualquiera \n       2.Cualquiera publica\n       3.Para bicicletas\n       4.Carretera \n       5.Solo para peatones") 


tipo_via=int(input(" \nElige el tipo de vía con la que dibujar el mapa (número):"))

while tipo_via<1 or tipo_via>5:
    print("ERROR: Opción no válida")
    tipo_via=int(input(" \nVuelve a elegir tipo de vía con la que dibujar el mapa (número):"))

if tipo_via==1:
    res="all"
elif tipo_via==2:
    res="all_public"
elif tipo_via==3:
    res="bike"
elif tipo_via==4:
    res="drive" 
elif tipo_via==5:
    res="walk"

#Crea el grafo de la ciudad con las carácterísticas indicadas por el usuario
mapa= ox.graph_from_place(ciudad, network_type=res)

#Añade el atributo "distancia" a cada arista del grafo. Después dibuja el grafo
mapa_con_dist=ox.distance.add_edge_lengths(mapa)
ox.plot_graph(mapa_con_dist)

#Le pedimos ambas direcciones, final e inicial, al usuario y obtenemos la latitud y longitud de cada una.
direccion_inicial=str(input("Introduce la dirección INICIAL (calle, ciudad, país):"))
direccion_final=str(input("Introduce la dirección FINAL (calle, ciudad, país):"))

location_inicial=geolocator.geocode(f"{direccion_inicial}")
location_final=geolocator.geocode(f"{direccion_final}")

if location_inicial:
    latitud_i=location_inicial.latitude
    longitud_i=location_inicial.longitude
else:
    print("ERROR: Dirección  inicial no encontrada")

if location_final:
    latitud_f=location_final.latitude
    longitud_f=location_final.longitude
else:
    print("ERROR: Dirección final no encontrada")

#Obtenemos cuales son los nodos mas cercanos a esas direcciones.
nodo_inicial=ox.nearest_nodes(mapa,longitud_i,latitud_i,return_dist=True)
nodo_final=ox.nearest_nodes(mapa,longitud_f,latitud_f,return_dist=True)

#Calculamos la ruta mas corta entre el nodo inicial y el nodo final. Devuelve una lista con los nodos en orden de recorrido.
ruta_final=ox.shortest_path(mapa,nodo_inicial[0],nodo_final[0])

#Imprimimos el grafo de la ciudad con la ruta final señalizada
ox.plot_graph_route(mapa,ruta_final,route_color='r',route_linewidth=4,route_alpha=1,orig_dest_size=100)

#Calcula e imprime la distancia total final a recorrer
dist_total=0
dist_nod_ini=nodo_inicial[1]
dist_nod_fin=nodo_final[1]
"""
for i in range(0,len(ruta_final)):
    if i == 0:
        None

    elif i==1:
        x_ini=ruta_final[0][]
        y_ini=ruta_final[0][]
        x_fin=ruta_final[i][]
        y_fin=ruta_final[i][]
        dist_total+= ox.distance.euclidean()

    else:
        x_ini=ruta_final[i-1][]
        y_ini=ruta_final[i-1][]
        x_fin=ruta_final[i][]
        y_fin=ruta_final[i][]
        dist_total+= ox.distance.euclidean()
"""
"""dist_total_final=dist_total+dist_nod_fin+dist_nod_ini


print(f"La distancia total a recorrer es de {dist_total_final/1000:.3f } kilómetros siguiendo el tipo de vía: {res} ")"""
