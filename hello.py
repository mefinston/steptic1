def app (environ, start_response):
   data = b"Hello, World!229 \n"
   start_response("200 OK", [ 
      ("Content-Type", "text/plain"),
   ])

   if environ["QUERY_STRING"] == '':
      data = data+"qery pust"
   else:
      query = str(environ["QUERY_STRING"])
      query = query.replace("&","\n")
      data = data+query
   return iter([data])    
