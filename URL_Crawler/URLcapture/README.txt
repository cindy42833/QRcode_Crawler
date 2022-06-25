# Crwal links and generate results
scrapy crawl example -a input=<input_name.csv> -s output=<output_name.csv> -s MONGODB_URI=<Mongodb_URL> -s MONGODB_DATABASE=<DATABASE_NAME> -s layer=<Layer>

e.g. input: root_cat1.csv, output: first_cat1.csv, MONGODB_URI: mongodb://localhost:27017, MONGODB_DATABASE: research, layer: 1
scrapy crawl example -s output=first_cat1.csv -a input=root_cat1.csv -s MONGODB_URI="mongodb://localhost:27017" -s MONGODB_DATABASE="research" -s layer=1
