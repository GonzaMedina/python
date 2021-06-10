   const apiKey = "evBITOfxuPCyEAWxt4AOcvKMfdsnfG88"; 

   //http://api.giphy.com/v1/gifs/random?api_key=Qj8o1u81YYQCeiLE5EALwjiGvbax3Sqn
   
   const peticion = fetch(`http://api.giphy.com/v1/gifs/random?api_key=${apiKey}`)
       peticion
           .then(respuesta=>respuesta.json())
           .then(({data}) => {
               const{url}= data.images.original
               //console.log(url)
               const img = document.createElement("img");
               img.src = url;
               document.body.append(img)
       })
       .catch (console.warn)

