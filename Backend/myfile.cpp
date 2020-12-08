problem : thumbnail not showing
reason : og-meta tags not changing 
websites read:

https://angular.io/guide/universal
https://stackoverflow.com/questions/54459617/adding-updating-meta-tags-not-working-in-angular-6
https://www.ngdevelop.tech/dynamically-add-title-and-meta-tags-on-route-change-in-angular/
https://www.xspdf.com/resolution/51679140.html
https://bugsdb.com/_en/debug/0b6d40c577cd8040a366ba641d167252
https://www.tektutorialshub.com/angular/dynamic-meta-tags-in-angular/
https://stackoverflow.com/questions/48330535/dynamically-add-meta-description-based-on-route-in-angular
https://fireflysemantics.medium.com/setting-angular-component-title-and-meta-tags-dynamically-71e76652fd9
https://www.thirdrocktechkno.com/blog/prerendering-in-angular-9/
https://www.cnc.io/en/blog/angular-server-side-rendering


the whatsapp and facebook thumbnail are generated through og meta tags
there is a function written in .ts file which changes meta tag according to the current page
function works fine and changes meta tags correctly
if we do inspect element , we can see correct tags being displayed
BUT if we do view source , it shows the meta tags of index.html
the main problem is the way the page is being rendered--CSR
the fb,whatsapp web crawlers probably cannot render the angular script and hence read the meta tags BEFORE they are changed 
one solution is to render the whole page at server(ssr) and then send it to the user
wccms website somewhat does this by rendering the header of the website on the server side and rest on the client side 
since the meta tags are in the header, it solves our problem
read both the repo's but was unable to find the difference