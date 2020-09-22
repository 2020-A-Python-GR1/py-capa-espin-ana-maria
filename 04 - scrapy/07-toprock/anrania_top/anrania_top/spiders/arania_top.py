import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class AraniaCrawlOnu (CrawlSpider):
	name = 'crawl_hotel'
	
	allowed_domains = ['booking.com']
	
	start_urls = [
		'https://www.booking.com/searchresults.es.html?aid=376374&label=esrow-OtlvhU2CXhSVxek50Z_17wS267754636757%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9069516%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcUSe6BbHz0Ad_yDShFFSHQ&sid=3112e7e892b7f81d1fca8104b4c1bc5c&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.es.html%3Faid%3D376374%3Blabel%3Desrow-OtlvhU2CXhSVxek50Z_17wS267754636757%253Apl%253Ata%253Ap1%253Ap22.563.000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-65526620%253Alp9069516%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YcUSe6BbHz0Ad_yDShFFSHQ%3Bsid%3D3112e7e892b7f81d1fca8104b4c1bc5c%3Bsb_price_type%3Dtotal%26%3B&ss=Entrada+principal+del+Europa+Park%2C+Rust%2C+Baden-Wurtemberg%2C+Alemania&is_ski_area=0&checkin_year=2020&checkin_month=10&checkin_monthday=1&checkout_year=2020&checkout_month=10&checkout_monthday=2&group_adults=1&group_children=1&no_rooms=1&age=0&b_h4u_keep_filters=&from_sf=1&ss_raw=europa&ac_position=0&ac_langcode=es&ac_click_type=b&dest_id=1589&dest_type=landmark&place_id_lat=48.2689618404014&place_id_lon=7.72144138813019&search_pageview_id=db0510cc2f8600ba&search_selected=true',
		'https://www.booking.com/searchresults.es.html?aid=376374&label=esrow-OtlvhU2CXhSVxek50Z_17wS267754636757%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9069516%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcUSe6BbHz0Ad_yDShFFSHQ&sid=3112e7e892b7f81d1fca8104b4c1bc5c&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.es.html%3Faid%3D376374%3Blabel%3Desrow-OtlvhU2CXhSVxek50Z_17wS267754636757%253Apl%253Ata%253Ap1%253Ap22.563.000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-65526620%253Alp9069516%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YcUSe6BbHz0Ad_yDShFFSHQ%3Bsid%3D3112e7e892b7f81d1fca8104b4c1bc5c%3Btmpl%3Dsearchresults%3Bac_click_type%3Db%3Bac_position%3D0%3Bage%3D0%3Bcheckin_month%3D10%3Bcheckin_monthday%3D1%3Bcheckin_year%3D2020%3Bcheckout_month%3D10%3Bcheckout_monthday%3D2%3Bcheckout_year%3D2020%3Bclass_interval%3D1%3Bdest_id%3D1589%3Bdest_type%3Dlandmark%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D1%3Bgroup_children%3D1%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dlandmark%3Broom1%3DA%252C0%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dindex%3Bsrc_elem%3Dsb%3Bsrpvid%3D362710e1e1a2005c%3Bss%3DEntrada%2520principal%2520del%2520Europa%2520Park%252C%2520Rust%252C%2520Baden-Wurtemberg%252C%2520Alemania%3Bss_all%3D0%3Bss_raw%3Deuropa%3Bssb%3Dempty%3Bsshis%3D0%3Btop_ufis%3D1%26%3B&ss=Entrada+principal+del+Europa+Park&is_ski_area=0&ssne=Entrada+principal+del+Europa+Park&ssne_untouched=Entrada+principal+del+Europa+Park&landmark=1589&checkin_year=2020&checkin_month=10&checkin_monthday=1&checkout_year=2020&checkout_month=10&checkout_monthday=2&group_adults=2&group_children=2&age=4&age=12&no_rooms=2&from_sf=1'
		]
	
	
	url_segmento_permitido = ('page')
	
	regla_dos = (##busca dentro de dominios
			Rule( ## permitidos y segmentos permitidos
					LinkExtractor(
						allow_domains = allowed_domains,
						allow = url_segmento_permitido				
					), callback = 'parse_page'		
				),	
	)
				
	rules = regla_dos #heredado (override)
	
	def parse_page(self, response):
		
		nombre_hotel = response.xpath('//span[@class = "sr-hotel__name"]').extract()
		recomendado = response.xpath('//h4[@class = "sr-group-recommendation__title sr-group-recommendation__title_biggest"]').extract()
		comentarios = response.xpath('//div[@ class ="bui-review-score__text"]').extract()
		precios = response.xpath('//div[@ class ="bui-review-score__text"]').extract() 
		puntuacion = response.xpath('//div[@ class ="bui-review-score__badge"]').extract()
		es = response.xpath('//div[@ class ="bui-review-score__title"]').extract()
		tipo_alojamiento = response.xpath('//span[@class="bui-badge bh-property-type bh-property-type--constructive-dark"]').extract()
        		
		serie_nombre_hotel = pd.Series(nombre_hotel)
		serie_recomendado = pd.Series(recomendado)
		serie_comentarios = pd.Series(comentarios)
		serie_precios = pd.Series(precios)
		serie_puntuacion = pd.Series(puntuacion)
		serie_es = pd.Series(es)
		serie_tipo = pd.Series(tipo_alojamiento)
		
		
		df = pd.DataFrame({"NOMBRE": serie_nombre_hotel,"RECOMENDADO":serie_recomendado , "COMENTARIOS": serie_comentarios,
		"PRECIOS": serie_precios, "PUNTUACION":serie_puntuacion, "CATALOGADO":serie_es, "TIPO ALOJAMIENTO":serie_tipo})
			
		
		#path_guardado = './datosIphone.xlsx'
		#df_Libro = df.copy()
		#df_Libro.to_excel(path_guardado, index = False)
		
		
		path_guardado = './datosbooking.csv'
		df_datos = df.copy()
		df_datos.to_csv(path_guardado, index = False)