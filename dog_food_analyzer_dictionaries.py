# This dictionary represents CO2 emission values in kilograms per 1000 kilocalories (kcal) for each diet category.
# These values are used to calculate the CO2 emissions of an ingredient panel based on the selected category.
# They are also used to calculate the CO2 emissions of a dog based on the daily calorie requirement and selected category.
dict_diet_category_emission_value = {"Dry":[4.25, "more than one-third of CO2eq emitted by an average human being"],
    "Wet":[33.56, "almost three times the CO2eq emitted by an average human being"]}


# Food category names
dict_diet_category_desc = {"Dry":"Dry Food Diet",
    "Wet":"Wet Food Diet"}


# Dictionary representing CO2 emission reduction factors for different dog food categories
# eg. Dry: we will help to reduce the co2 emission by calorie intake of dog by 10 times
reducing_co2_dict = {"Dry": 10,
    "Wet": 50}


# Dictionary mapping factors to their corresponding CO2 emissions in metric tons and units.
# Format: {Factor: [CO2 in metric tonnes, unit]}
# These values are used to calculate the equivalence of CO2 emissions by ingredients and dog's calorie to other factors.
other_factors_of_co2_in_metric_tons = {
    'miles_of_gasoline_vehicle' : [0.00039, 'CO2E/mile'], 
    'barrells_of_oil_consumed' : [0.43, 'CO2/barrel'],
    'number_of_urban_tree_seedlings_grown' : [0.060 ,'CO2/urban tree planted'],
    'pounds_of_coal_burnt' : [0.000893, 'CO2/pound of coal'],
    'carbon_sequestered_in_one_year_by_one_acre' : [0.84, 'CO2/acre/year']
    }


# Dictionary specifying the thresholds for the green to red bars.
# The calculated CO2 values will fall within these ranges.
threshold_of_ingredient_dict = {"Dry": [0, 9],
    "Wet": [22, 42]}



# Dictionary used to determine the proportion of the top ingredients.
# The keys 1 to 5 represent the length of the ingredient panel.
# If the length is 1 to 5, the 100% proportion will be divided those among the ingredients.
# If the length exceeds 5, the proportions will be divided by food category, with the top ingredients receiving 85% of the total proportion.
proportion_division_dict = {
 1: [100.0],
 2: [70.0, 30.0],
 3: [55.0, 30.0, 15.0],
 4: [40.0, 25.0, 22.0, 14.0],
 5: [35.0, 25.0, 23.0, 10.0, 7.0],
 'Wet': [20.0, 18.0, 13.0, 11.0, 8.0, 6.0, 5.0, 4.0],
 'Dry': [11.0, 11.0, 11.0, 10.0, 10.0, 9.0, 8.0, 5.0, 4.0, 4.0, 3.0]}


# Dictionary specifying the average lifespan of each dog breed.
# Lifespan is used to calculate the dog's life stage, as calorie requirements depend on the age/life stage of the dog.
dog_breed_lifespan = {'Affenpinscher': 14,
 'Afghan Hound': 14,
 'African Boerboels': 11,
 'Airedale Terrier': 13,
 'Akbash': 11,
 'Akita': 13,
 'Alapaha Blue Blood Bulldogs': 13,
 'Alaskan Klee Kai': 14,
 'Alaskan Malamute': 13,
 'American Bulldog': 14,
 'American Eskimo Dog': 14,
 'American Foxhound': 13,
 'American Staffordshire Terrier': 14,
 'American Water Spaniel': 12,
 'Anatolian Shepherd Dog': 13,
 'Australian Cattle Dog': 13,
 'Australian Kelpie': 12,
 'Australian Shepherd': 15,
 'Australian Silky Terrier': 14,
 'Australian Terrier': 14,
 'Basenji': 14,
 'Basset Hound': 14,
 'Beagle': 14,
 'Bearded Collie': 14,
 'Beauceron': 12,
 'Bedlington Terrier': 14,
 'Belgian Malinois': 12,
 'Belgian Shepherd Dog': 12,
 'Belgian Tervuren': 12,
 'Bernese Mountain Dog': 9,
 'Bichon Frise': 15,
 'Black and Tan Coonhound': 12,
 'Black Russian Terrier': 11,
 'Bloodhound': 12,
 'Border Collie': 14,
 'Border Terrier': 15,
 'Borzoi': 12,
 'Boston Terrier': 14,
 'Bouvier des Flandres': 12,
 'Boxer': 10,
 'Briard': 12,
 'Brittany': 13,
 'Brussels Griffon': 15,
 'Bull Terrier': 14,
 'Bullmastiff': 10,
 'Cairn Terrier': 14,
 'Canaan Dog': 13,
 'Cane Corso': 11,
 'Cardigan Welsh Corgi': 14,
 'Carolina Dog': 13,
 'Catahoula Leopard Dogs': 12,
 'Cavalier King Charles Spaniel': 14,
 'Central Asian Ovtcharkas': 12,
 'Cesky Terrier': 14,
 'Chesapeake Bay Retriever': 13,
 'Chihuahua': 18,
 'Chinese Crested': 15,
 'Chinese Foo': 11,
 'Chinese Shar-Pei': 10,
 'Chipoo': 14,
 'Chow Chow': 12,
 'Clumber Spaniel': 12,
 'Cocker Spaniel': 15,
 'Cockapoo': 18,
 'Collie': 12,
 'Coton De Tulears': 15,
 'Curly-Coated Retriever': 12,
 'Dachshund': 14,
 'Dalmatian': 14,
 'Dandie Dinmont Terrier': 13,
 'Doberman Pinscher': 12,
 'Dogue de Bordeaux': 7,
 'English Bulldogs': 12,
 'English Cocker Spaniels': 14,
 'English Foxhound': 13,
 'English Setter': 12,
 'English Shepherd': 15,
 'English Springer Spaniel': 14,
 'English Toy Spaniel': 12,
 'Estrela Mountain Dogs': 11,
 'Field Spaniel': 14,
 'Fila Brasileiros': 10,
 'Finnish Spitz': 14,
 'Flat-Coated Retriever': 13,
 'Fox Terrier (Smooth)': 13,
 'Fox Terrier (Wire)': 13,
 'French Bulldog': 11,
 'German Pinscher': 15,
 'German Shepherd': 12,
 'German Shorthaired Pointer': 14,
 'German Wirehaired Pointer': 14,
 'Giant Schnauzer': 12,
 'Glen of Imaal Terrier': 14,
 'Golden Retriever': 13,
 'Goldendoodle': 14,
 'Gordon Setter': 12,
 'Great Dane': 10,
 'Great Pyrenees': 12,
 'Greater Swiss Mountain Dog': 12,
 'Greyhound': 13,
 'Harrier': 14,
 'Havanese': 14,
 'Hungarian Vizsla': 14,
 'Ibizan Hound': 14,
 'Irish Setter': 14,
 'Irish Terrier': 15,
 'Irish Water Spaniel': 13,
 'Irish Wolfhound': 7,
 'Italian Greyhound': 15,
 'Jack Russell Terrier': 13,
 'Japanese Chin': 14,
 'Keeshond': 14,
 'Kerry Blue Terrier': 15,
 'Komondor': 12,
 'Kooikerhondje': 13,
 'Kuvasz': 12,
 'Labradoodle': 13,
 'Labrador Retriever': 12,
 'Laekenois': 12,
 'Lakeland Terrier': 16,
 'Lancashire Heeler': 14,
 'Lhasa Apso': 14,
 'Löwchen': 15,
 'Maltese': 14,
 'Maltipoo': 13,
 'Manchester Terrier': 16,
 'Maremma Sheepdog': 12,
 'Mastiff': 11,
 'Miniature Bull Terrier': 14,
 'Miniature Pinscher': 14,
 'Miniature Poodle': 14,
 'Miniature Schnauzer': 14,
 'Neapolitan Mastiff': 10,
 'Newfoundland': 10,
 'Norfolk Terrier': 15,
 'Norwegian Buhunds': 13,
 'Norwegian Elkhound': 12,
 'Norwich Terrier': 15,
 'Nova Scotia Duck Tolling Retriever': 13,
 'Old English Sheepdog': 12,
 'Otterhound': 13,
 'Papillon': 15,
 'Parson Russell Terrier': 15,
 'Peekapoo': 13,
 'Pekingese': 15,
 'Pembroke Welsh Corgi': 13,
 'Petit Basset Griffon Vendeen': 14,
 'Pharaoh Hound': 14,
 'Pit Bull': 14,
 'Plott': 13,
 'Pointer': 5,
 'Polish Lowland Sheepdog': 14,
 'Pomapoo': 13,
 'Pomeranian': 16,
 'Poodle (Standard)': 15,
 'Portuguese Water Dog': 14,
 'pug': 15,
 'puli': 15,
 'Rat Terrier': 16,
 'Redbone Coonhound': 11,
 'Rhodesian Ridgeback': 12,
 'Rottweiler': 11,
 'Saint Bernard': 10,
 'Saluki': 14,
 'Samoyed': 12,
 'Schipperke': 15,
 'Schnoodle': 13,
 'Scottish Deerhound': 9,
 'Scottish Terrier': 13,
 'Sealyham Terrier': 13,
 'Shetland Sheepdog': 14,
 'Shiba Inu': 15,
 'Shih Tzu': 14,
 'Siberian Husky': 13,
 'Silky Terrier': 14,
 'Skye Terrier': 14,
 'Snorkie': 12,
 'Soft-coated Wheaten Terrier': 14,
 'Spinone Italiano': 14,
 'Staffordshire Bull Terrier': 14,
 'Standard Schnauzer': 14,
 'Sussex Spaniel': 13,
 'Swedish Vallhund': 13,
 'Thai Ridgeback': 12,
 'Tibetan Mastiff': 14,
 'Tibetan Spaniel': 14,
 'Tibetan Terrier': 15,
 'Toy Fox Terrier': 14,
 'Toy Manchester Terrier': 16,
 'Toy Poodle': 14,
 'Treeing Walker Coonhound': 13,
 'Vizsla': 14,
 'Weimaraner': 13,
 'Welsh Springer Spaniel': 15,
 'West Highland White Terrier': 14,
 'Whippet': 15,
 'Wirehaired Pointing Griffon': 14,
 'Xoloitzcuintle': 13,
 'Yorkie-Poo': 14,
 'Yorkshire Terrier': 16}

# Dictionary used for cleaning ingredient strings.
# The 'cleaning_dictionary' is a nested dictionary where the keys represent the noises or unclean chunks that might be present in the ingredient strings,
# and the values represent the corresponding cleaned chunks.
cleaning_dictionary = {'Cat Dry Food': {'ingredients\\n                                    \n                             ': '',
        '] vitamins [': ', ',
        '. contains a source of live naturally occurring microorganisms.': ', natural microorganisms',
        '. contains a source of live (viable), naturally occurring microorganisms.': ', natural microorganisms',
        'docosahexaenoic acid (dha)': 'docosahexaenoic acid',
        'mixed tocopherols (vitamin e) used as a preservative': 'mixed tocopherols (preservative)',
        'animal fat preserved with mixed-tocopherols (form of vitamin e)': 'animal fat (preserved with mixed-tocopherols)',
        'mixed tocopherols (preservative, form of vitamin e;': 'mixed tocopherols (preservative and a form of vitamin e)',
        '\\n': ' ',
        'menadione, sodium bisulfite complex': 'menadione sodium bisulfite complex',
        'thiamine, mononitrate': 'thiamine mononitrate',
        ')': '),',
        ',,': ',',
        'vitamin e supplement  niacin  thiamine mononitrate  d-pantothenic acid  vitamin a supplement  riboflavin  pyridoxine hydrochloride  biotin  vitamin b12 supplement  vitamin d3 supplement  folic acid': 'vitamin e supplement, niacin, thiamine mononitrate, d-pantothenic acid, vitamin a supplement, riboflavin, pyridoxine hydrochloride, biotin, vitamin b12 supplement, vitamin d3 supplement, folic acid',
        'zinc proteinate  iron proteinate  calcium carbonate  manganese proteinate  copper proteinate  sodium selenite  calcium iodate': 'zinc proteinate, iron proteinate, calcium carbonate, manganese proteinate, copper proteinate, sodium selenite, calcium iodate',
        'contains a source of live, naturally occurring microorganisms': '',
        '*': '',
        ', preserved with natural mixed tocopherols and citric acid': ', mixed tocopherols (preservative), citric acid',
        '\\n                        ': '',
        'biotin) minerals (': 'biotin), (',
        'chicken & rice:': '',
        '         meal': '',
        '   a-2569': ' a-2569',
        '\\n ': ' ',
        '\\xa0': ' ',
        'essential nutrients and other ingredients: ': '',
        '        inactive ingredients: disodium edta': ' disodium edta',
        'dried bacillus coagulans, fermentation product.': 'dried bacillus coagulans fermentation product',
        ';': '\\n',
        '[': '',
        ']': '',
        'new:': '',
        ' ,': ',',
        '*(official name is marine microalgae)': '',
        '\\u200btrout': ' ',
        '?': ' ',
        '\\u202f': ' ',
        '\\t': ',',
        'a639120': '',
        'bisul\\x1ete': 'bisulfite',
        'disulfite': 'bisulfite',
        'minerals': '',
        'vitamins': '',
        ' b626618-13': '',
        'sa�owerr oil': 'safflower oil',
        'boneless, skinless': 'boneless skinless',
        'sa\\x1dower oil': 'safflower oil',
        '(l-ascorbyl-2-polyphosphate (source of vitamin c)': 'l-ascorbyl-2-polyphosphate',
        'l-ascorbyl-2-polyphosphate (source of vitamin c)': 'l-ascorbyl-2-polyphosphate',
        'alltech™ probiotics: ': '',
        'biotin) (copper sulfate': 'biotin, copper sulfate',
        'dehydrated sweet orange dehydrated apple': 'dehydrated sweet orange, dehydrated apple',
        'and dried': ', dried',
        'contains a source of live (viable)': '',
        'poultry fat from 100% chicken mixed tocopherols (preservative)': 'poultry fat from 100% chicken (preserved with mixed tocopherols)',
        'animal fat (preserved with mixed-tocopherols)': 'animal fat (preserved with mixed tocopherols)',
        'beef fat preserved with mixed tocopherols': 'beef fat (preserved with mixed tocopherols)',
        'canola oil (preserved with mixed tocopherols source of vitamin e)': 'canola oil (preserved with mixed tocopherols)',
        'catfish oil preserved with mixed tocopherols': 'catfish oil (preserved with mixed tocopherols)',
        'chicken fat (preserved with mixed natural tocopherols source of vitamin e)': 'chicken fat (preserved with natural mixed tocopherols)',
        'docosahexaenoic acid (source of omega-3 fatty acids)': 'dha (source of omega-3 fatty acids)',
        'feed grade fat product (algae source of fatty acids)': 'feed grade fat product algae',
        'fish oil from 100% menhaden oil mixed tocopherols (preservative)': 'menhaden fish oil (preserved with mixed tocopherols)',
        'a- ': 'a',
        'ground miscanthus gra ss': 'ground miscanthus grass',
        'herring oil (preserved with mixed tocopherols source of vitamin e)': 'herring oil (preserved with mixed tocopherols)',
        'menhaden fish oil (preserved with mixed natural tocopherols source of vitamin e)': 'menhaden fish oil (preserved with mixed tocopherols)',
        'poultry fat from 100% chicken (preserved with mixed tocopherols)': 'chicken fat (preserved with mixed tocopherols)',
        'taurin,': 'taurine,',
        'vegetable juice (color)': 'vegetable juice',
        'preserved with mixed tocopherols and citric acid': 'preserved with mixed tocopherols, and citric acid',
        ', source': ' source',
        ', a source': ' source',
        'potassium iodide (beta-carotene': 'potassium iodide, beta-carotene',
        'rosemary extract and spearmint': 'rosemary extract, spearmint',
        'pyridoxine, calcium iodate': 'pyridoxine hydrochloride, calcium iodate',
        'vitamin d3 supplement. folic acid': 'vitamin d3 supplement, folic acid',
        'white fish meal (pacific whiting': 'pacific whiting',
        ' +': ' ',
        'sa\x1dower': 'safflower',
        'bisul\x1ete': 'bisulfate'},
        'Dog Wet Food': {'new:': '', 'vitamen': 'vitamin',
                         'vitamon': 'vitamin',
                         
        'iron amino acid chelate  vitamin e supplement': 'iron amino acid chelate, vitamin e supplement',
                         
        'iron proteinate  copper proteinate': 'iron proteinate, copper proteinate',
                         
        'vitamin e supplement niacin vitamin a supplement thiamine mononitrate riboflavin': 'vitamin e supplement, niacin, vitamin a supplement, thiamine mononitrate, riboflavin',
                         
        'calcium iodate and selenium yeast': 'calcium iodate, selenium yeast',
                         
        'copper proteinate manganese proteinate calcium iodate': 'copper proteinate, manganese proteinate, calcium iodate',
                         
        'magnesium sulfate. sodium selenite': 'magnesium sulfate, sodium selenite',
                         
        "pea starch\\xa0 brewer's dried yeast": "pea starch, brewer's dried yeast",
                         
        'potato calcium carbonate': 'potato, calcium carbonate',
                         
        'pyridoxine hydrochloride vitamin d3 supplement': 'pyridoxine hydrochloride, vitamin d3 supplement',
        'biotin vitamin b12 supplement folic acid vitamin d3 supplement d-calcium pantothenate taurine kale blueberries raspberries cranberries carrots': 'biotin, vitamin b12 supplement, folic acid, vitamin d3 supplement, d-calcium pantothenate, taurine, kale, blueberries, raspberries, cranberries, carrots',
        'riboavin': 'riboflavin',
        'boneless turkey water sufficient for processing rice salt calcium carbonate monodicalcium phosphate choline chloride potassium chloride zinc proteinate iron proteinate': 'boneless turkey, water sufficient for processing, rice, salt, calcium carbonate, monodicalcium, phosphate, choline chloride, potassium chloride, zinc proteinate, iron proteinate',
        'riboflavin  biotin': 'riboflavin, biotin',
        'magnesium sulfate. choline chloride': 'magnesium sulfate, choline chloride',
        'rice pasta (rice, water, ground tapioca)': 'rice pasta',
        'salmo,': 'salmon,',
        ', supplement': ' supplement',
        'thiamine mononitrate {vitamin b1} d-calcium pantothenate': 'thiamine mononitrate (vitamin b1), d-calcium pantothenate',
        'turkey & bacon\\n': '',
        'turkey & duck\\n': '',
        'vitamin b12 pyridoxine hydrochloride': 'vitamin b12, pyridoxine hydrochloride',
        'supplement.  water': 'supplement, water',
        ',vitamins': ',',
        'water sufficient for\\nprocessing': 'water sufficient for processing',
        'supplement. water': 'supplement, water',
        'natural flavor cranberries': 'natural flavor, cranberries',
        'vitamins & minerals': '',
        'dicalcium phosphate minerals': 'dicalcium phosphate, minerals',
        'ground flaxseed choline chloride': 'ground flaxseed, choline chloride',
        'icelandic fish (cod': '(cod',
        'natural hickory smoke': 'natural hickory smoke flavor',
        'pyridoxine hydrochloride,(vitamin b6)': 'pyridoxine hydrochloride (vitamin b6)',
        'vitamin e, a, b12, d3': 'vitamin e, vitamin a, vitamin b12, vitamin d3',
        'apples rice starch': 'apples, rice starch',
        'beef fat(preserved with mixed tocopherols and ascorbic acid)': 'beef fat (preserved with mixed tocopherols and ascorbic acid)',
        'bitoin': 'biotin',
        'calcium , pantothenate': 'calcium pantothenate',
        '. contains a source of live (viable), naturally occurring microorganisms.': '',
        'this is a naturally preserved product': '',
        'this is a naturally preserved product.': '',
        'spearmint extract.\\nthis is a naturally preserved product.': 'spearmint extract',
        'spearmint extract.this is a naturally preserved product.': 'spearmint extract',
        'spearmint extract. this is a naturally preserved product.': 'spearmint extract',
        'tomato pomace  chicken fat (mixed tocopherols)': 'tomato pomace, chicken fat (preserved with mixed tocopherols)',
        'vegetavle': 'vegetable',
        'vitamin b12 supplement) dried': 'vitamin b12 supplement), dried',
        'ï¿½': ' ',
        ') citric acid': '), citric acid',
        'vitamin d3 supplement) mixed tocopherols for freshness': 'vitamin d3 supplement), mixed tocopherols for freshness',
        'yeast extract (a source of prebiotics) glucosamine hydrochloride': 'yeast extract (a source of prebiotics), glucosamine hydrochloride',
        'oatmeal barley': 'oatmeal, barley',
        'ocean \\x1dfish meal': 'ocean fish meal',
        '. d-2620. 15% - a source of fiber.': '',
        'psyilium seed husks taurine calcium carbonate vitamin e supplement': 'psyllium seed husk, taurine, calcium carbonate, vitamin e supplement',
        'pyri- doxine hydrochloride (vitamin b6)': 'pyridoxine hydrochloride (vitamin b6)',
        ' reserved with mixed tocopherols and citric acid.': 'mixed tocopherols (preservative), citric acid (preservative)',
        'powered cellulose': 'powdered cellulose',
        'riboâ€‚avin': 'riboflavin',
        'rosemary extract supplement, ': '',
        'zinc sulfate ferrous sulfate': 'zinc sulfate, ferrous sulfate',
        'dried bacillus coagulans, fermentation product.': 'dried bacillus coagulans fermentation product',
        '.\\ncontains a source of live (viable), naturally occurring microorganisms.': '',
        'lactosaccâ„¢ probiotics:': '',
        'mixed tocopherols (preservative ,': 'mixed tocopherols (preservative),',
        'natural vegetable flavor dicalcium phosphate': 'natural vegetable flavor, dicalcium phosphate',
        'rosemary.': 'rosemary',
        'salt vitamins': 'salt, vitamins',
        'canolia oil (preserved with mixed tocopherols)': 'canola oil (preserved with mixed tocopherols)',
        'carrageenan guar gum': 'carrageenan, guar gum',
        'cobalt amino acid, chelate': 'cobalt amino acid chelate',
        'copper proteinate sodium selenite': 'copper proteinate, sodium selenite',
        'lecithin and rosemary extract': 'lecithin, rosemary extract',
        'hydrolyzed yeast (actigenâ„¢ - prebiotic)': 'hydrolyzed yeast',
        'pyridoxine, hydrochloride': 'pyridoxine hydrochloride',
        'dlâ€“methionine': 'dl-methionine',
        'â  ': '',
        'â': '',
        'the facility in which this food is made also makes food that may contain other': '',
        'animal fat, (source of omega 6 fatty acids [preserved with bha/citric acid])': 'animal fat (preserved with bha & citric acid)',
        'animal fat, (source of omega 6 fatty acids) [preserved with bha/citric acid]': 'animal fat (preserved with bha & citric acid)',
        'd-calcium pantothenate, [source of vitamin b5]': 'd-calcium pantothenate (source of vitamin b5)',
        'niacin, (vitamin b-3)': 'niacin (vitamin b-3)',
        'chicken fat (preserved with mixed natural tocopherols, a source of vitamin e)': 'chicken fat (preserved with mixed natural tocopherols)',
        'tocopherols, a source of vitamin e': 'tocopherols',
        'animal fat (source of omega 6 fatty acids) [preserved with bha and citric acid])': 'animal fat (preserved with bha and citric acid)',
        'bha and citric acid (a preservative)': 'bha (preservative), citric acid (preservative)',
        'biotin folic acid': 'biotin, folic acid',
        '€™': '',
        'cobalt, carbonate': 'cobalt carbonate',
        'chicken by-products (organs only, source of arginine)': 'chicken by-products',
        'chicken fat (preserved with natural mixed tocopherols; a source of vitamin e)': 'chicken fat (preserved with natural mixed tocopherols)',
        'chicken meal (natural source of glucosamine and chondroitin)': 'chicken meal',
        'cobalt carbonate and cobalt glucoheptonate': 'cobalt carbonate, cobalt glucoheptonate',
        'cobalt carbonate) dried chicory root': 'cobalt carbonate), dried chicory root',
        'dl-methionine hydroxy analogue': 'dl-methionine',
        'dried bi€‚dobacterium animalis fermentation product': 'dried bifidobacterium animalis fermentation product',
        'dried lactobacillus acidophilus fermentation product rosemary extract': 'dried lactobacillus acidophilus fermentation product, rosemary extract',
        'contains a source of live naturally occuring microorganisms.': '',
        'dried lactobacillus casei fermentation product.': 'dried lactobacillus casei fermentation product',
        'dried lactobacillus plantarum fermentation product.': 'dried lactobacillus plantarum fermentation product',
        'folic acid] dl-methionine': 'folic acid], dl-methionine',
        'i-threonine': 'l-threonine',
        'menhaden fish meal (a source of glucosamine and chondroitin)': 'menhaden fish meal',
        'mixed tocopherols (a source of vitamin e) and rosemary extract.': 'mixed tocopherols (a source of vitamin e), rosemary extract',
        ',,': ',',
        'essential nutrients and other ingredients:': ',',
        '         meal': '',
        '\\xa0': ' ',
        ';': '\\n',
        ' ,': ',',
        '*(official name is marine microalgae)': '',
        '\\u200btrout': ' ',
        '?': ' ',
        '\\u202f': ' ',
        '\\t': ',',
        'a639120': '',
        ' minerals': '',
        ' vitamins': '',
        ' b626618-13': '',
        'riboflavin supplement vitamin,': 'riboflavin supplement, vitamin',
        'vitamin e, a, d3, b12 supplements,': 'vitamin e, vitamin a, vitamin d3, vitamin b12,',
        'folic acid inulin': 'folic acid, inulin',
        '(boneless, skinless breast)': '',
        '�': '',
        '"': '',
        '>': '',
        '<': '',
        ') vitamins (': '), (',
        ') minerals (': '), (',
        ', and ': ', ',
        ', preserved with mixed tocopherols and citric acid': ', preserved with mixed tocopherols, and citric acid',
        'minerals': '',
        '(, )': ',',
        '*': '',
        'ingredients': '',
        'cottage cheese (milk': 'cottage cheese, (milk ingredients',
        'sa�ower oil': 'safflower oil',
        'bonless, skinless': 'boneless skinless',
        'contains a source of live (viable) naturally occurring microorganisms': '',
        '\\n': '',
        'delivered fresh or raw': '',
        "dried bacillus coagulans fermentation product zinc proteinate',   'dried bacillus coagulans fermentation product, zinc proteinate'": '',
        "dried chicory root (source of inulin) dried pediococcus acidilactici fermentation product',   'dried chicory root (source of inulin), dried pediococcus acidilactici fermentation product'": '',
        '(proteinated and)': '',
        'potassium, chloride': 'potassium chloride',
        '(l-ascorbyl-2-polyphosphate (source of vitamin c)': 'l-ascorbyl-2-polyphosphate (source of vitamin c)',
        'chicken fat, (preserved with mixed tocopherols)': 'chicken fat (preserved with mixed tocopherols)',
        'animal fat, (source of omega 6 fatty acids (preserved with bha/citric acid))': 'animal fat (preserved with bha & citric acid)',
        '. ferrous sulfate': ' ferrous sulfate',
        '. peas': ' peas',
        'minerals magnesium oxide': 'magnesium oxide'},
        'Dog Dry Food': {'new:': '',
        'iron amino acid chelate  vitamin e supplement': 'iron amino acid chelate, vitamin e supplement',
        'iron proteinate  copper proteinate': 'iron proteinate, copper proteinate',
        'magnesium sulfate. sodium selenite': 'magnesium sulfate, sodium selenite',
        "pea starch\\xa0 brewer's dried yeast": "pea starch, brewer's dried yeast",
        'potato calcium carbonate': 'potato, calcium carbonate',
        'pyridoxine hydrochloride vitamin d3 supplement': 'pyridoxine hydrochloride, vitamin d3 supplement',
        'riboavin': 'riboflavin',
        'riboflavin  biotin': 'riboflavin, biotin',
        'rice pasta (rice, water, ground tapioca)': 'rice pasta',
        'salmo,': 'salmon,',
        ', supplement': ' supplement',
        'thiamine mononitrate {vitamin b1} d-calcium pantothenate': 'thiamine mononitrate (vitamin b1), d-calcium pantothenate',
        'turkey & bacon\\n': '',
        'turkey & duck\\n': '',
        'vitamin b12 pyridoxine hydrochloride': 'vitamin b12, pyridoxine hydrochloride',
        'supplement.  water': 'supplement, water',
        ',vitamins': ',',
        'water sufficient for\\nprocessing': 'water sufficient for processing',
        'supplement. water': 'supplement, water',
        'natural flavor cranberries': 'natural flavor, cranberries',
        'vitamins & minerals': '',
        'dicalcium phosphate minerals': 'dicalcium phosphate, minerals',
        'ground flaxseed choline chloride': 'ground flaxseed, choline chloride',
        'icelandic fish (cod': '(cod',
        'natural hickory smoke': 'natural hickory smoke flavor',
        'pyridoxine hydrochloride,(vitamin b6)': 'pyridoxine hydrochloride (vitamin b6)',
        'vitamin e, a, b12, d3': 'vitamin e, vitamin a, vitamin b12, vitamin d3',
        'apples rice starch': 'apples, rice starch',
        'beef fat(preserved with mixed tocopherols and ascorbic acid)': 'beef fat (preserved with mixed tocopherols and ascorbic acid)',
        'bitoin': 'biotin',
        'calcium , pantothenate': 'calcium pantothenate',
        '. contains a source of live (viable), naturally occurring microorganisms.': '',
        'this is a naturally preserved product': '',
        'this is a naturally preserved product.': '',
        'spearmint extract.\\nthis is a naturally preserved product.': 'spearmint extract',
        'spearmint extract.this is a naturally preserved product.': 'spearmint extract',
        'spearmint extract. this is a naturally preserved product.': 'spearmint extract',
        'tomato pomace  chicken fat (mixed tocopherols)': 'tomato pomace, chicken fat (preserved with mixed tocopherols)',
        'vegetavle': 'vegetable',
        'vitamin b12 supplement) dried': 'vitamin b12 supplement), dried',
        'ï¿½': ' ',
        ') citric acid': '), citric acid',
        'vitamin d3 supplement) mixed tocopherols for freshness': 'vitamin d3 supplement), mixed tocopherols for freshness',
        'yeast extract (a source of prebiotics) glucosamine hydrochloride': 'yeast extract (a source of prebiotics), glucosamine hydrochloride',
        'oatmeal barley': 'oatmeal, barley',
        'ocean \\x1dfish meal': 'ocean fish meal',
        '. d-2620. 15% - a source of fiber.': '',
        'psyilium seed husks taurine calcium carbonate vitamin e supplement': 'psyllium seed husk, taurine, calcium carbonate, vitamin e supplement',
        'pyri- doxine hydrochloride (vitamin b6)': 'pyridoxine hydrochloride (vitamin b6)',
        ' reserved with mixed tocopherols and citric acid.': 'mixed tocopherols (preservative), citric acid (preservative)',
        'powered cellulose': 'powdered cellulose',
        'riboâ€‚avin': 'riboflavin',
        'rosemary extract supplement, ': '',
        'zinc sulfate ferrous sulfate': 'zinc sulfate, ferrous sulfate',
        'dried bacillus coagulans, fermentation product.': 'dried bacillus coagulans fermentation product',
        '.\\ncontains a source of live (viable), naturally occurring microorganisms.': '',
        'lactosaccâ„¢ probiotics:': '',
        'mixed tocopherols (preservative ,': 'mixed tocopherols (preservative),',
        'natural vegetable flavor dicalcium phosphate': 'natural vegetable flavor, dicalcium phosphate',
        'rosemary.': 'rosemary',
        'salt vitamins': 'salt, vitamins',
        'canolia oil (preserved with mixed tocopherols)': 'canola oil (preserved with mixed tocopherols)',
        'carrageenan guar gum': 'carrageenan, guar gum',
        'cobalt amino acid, chelate': 'cobalt amino acid chelate',
        'copper proteinate sodium selenite': 'copper proteinate, sodium selenite',
        'lecithin and rosemary extract': 'lecithin, rosemary extract',
        'hydrolyzed yeast (actigenâ„¢ - prebiotic)': 'hydrolyzed yeast',
        'pyridoxine, hydrochloride': 'pyridoxine hydrochloride',
        'dlâ€“methionine': 'dl-methionine',
        'â  ': '',
        'â': '',
        'the facility in which this food is made also makes food that may contain other': '',
        'animal fat, (source of omega 6 fatty acids [preserved with bha/citric acid])': 'animal fat (preserved with bha & citric acid)',
        'animal fat, (source of omega 6 fatty acids) [preserved with bha/citric acid]': 'animal fat (preserved with bha & citric acid)',
        'd-calcium pantothenate, [source of vitamin b5]': 'd-calcium pantothenate (source of vitamin b5)',
        'niacin, (vitamin b-3)': 'niacin (vitamin b-3)',
        'chicken fat (preserved with mixed natural tocopherols, a source of vitamin e)': 'chicken fat (preserved with mixed natural tocopherols)',
        'tocopherols, a source of vitamin e': 'tocopherols',
        'animal fat (source of omega 6 fatty acids) [preserved with bha and citric acid])': 'animal fat (preserved with bha and citric acid)',
        'bha and citric acid (a preservative)': 'bha (preservative), citric acid (preservative)',
        'biotin folic acid': 'biotin, folic acid',
        '€™': '',
        'cobalt, carbonate': 'cobalt carbonate',
        'chicken by-products (organs only, source of arginine)': 'chicken by-products',
        'chicken fat (preserved with natural mixed tocopherols; a source of vitamin e)': 'chicken fat (preserved with natural mixed tocopherols)',
        'chicken meal (natural source of glucosamine and chondroitin)': 'chicken meal',
        'cobalt carbonate and cobalt glucoheptonate': 'cobalt carbonate, cobalt glucoheptonate',
        'cobalt carbonate) dried chicory root': 'cobalt carbonate), dried chicory root',
        'dl-methionine hydroxy analogue': 'dl-methionine',
        'dried bi€‚dobacterium animalis fermentation product': 'dried bifidobacterium animalis fermentation product',
        'dried lactobacillus acidophilus fermentation product rosemary extract': 'dried lactobacillus acidophilus fermentation product, rosemary extract',
        'contains a source of live naturally occuring microorganisms.': '',
        'dried lactobacillus casei fermentation product.': 'dried lactobacillus casei fermentation product',
        'dried lactobacillus plantarum fermentation product.': 'dried lactobacillus plantarum fermentation product',
        'folic acid] dl-methionine': 'folic acid], dl-methionine',
        'i-threonine': 'l-threonine',
        'menhaden fish meal (a source of glucosamine and chondroitin)': 'menhaden fish meal',
        'mixed tocopherols (a source of vitamin e) and rosemary extract.': 'mixed tocopherols (a source of vitamin e), rosemary extract',
        ',,': ',',
        'essential nutrients and other ingredients:': ',',
        '         meal': '',
        '\\xa0': ' ',
        ';': '\\n',
        ' ,': ',',
        '*(official name is marine microalgae)': '',
        '\\u200btrout': ' ',
        '?': ' ',
        '\\u202f': ' ',
        '\\t': ',',
        'a639120': '',
        ' minerals': '',
        ' vitamins': '',
        ' b626618-13': '',
        'riboflavin supplement vitamin,': 'riboflavin supplement, vitamin',
        'vitamin e, a, d3, b12 supplements,': 'vitamin e, vitamin a, vitamin d3, vitamin b12,',
        'folic acid inulin': 'folic acid, inulin',
        '(boneless, skinless breast)': '',
        '�': '',
        '"': '',
        '>': '',
        '<': '',
        ') vitamins (': '), (',
        ') minerals (': '), (',
        ', and ': ', ',
        ', preserved with mixed tocopherols and citric acid': ', preserved with mixed tocopherols, and citric acid',
        'minerals': '',
        '(, )': ',',
        '*': '',
        'ingredients': '',
        'cottage cheese (milk': 'cottage cheese, (milk ingredients',
        'sa�ower oil': 'safflower oil',
        'bonless, skinless': 'boneless skinless',
        'contains a source of live (viable) naturally occurring microorganisms': '',
        '\\n': '',
        'delivered fresh or raw': '',
        "dried bacillus coagulans fermentation product zinc proteinate',   'dried bacillus coagulans fermentation product, zinc proteinate'": '',
        "dried chicory root (source of inulin) dried pediococcus acidilactici fermentation product',   'dried chicory root (source of inulin), dried pediococcus acidilactici fermentation product'": '',
        '(proteinated and)': '',
        'potassium, chloride': 'potassium chloride',
        '(l-ascorbyl-2-polyphosphate (source of vitamin c)': 'l-ascorbyl-2-polyphosphate (source of vitamin c)',
        'chicken fat, (preserved with mixed tocopherols)': 'chicken fat (preserved with mixed tocopherols)',
        'animal fat, (source of omega 6 fatty acids (preserved with bha/citric acid))': 'animal fat (preserved with bha & citric acid)',
        '. ferrous sulfate': ' ferrous sulfate',
        '. peas': ' peas',
        'minerals magnesium oxide': 'magnesium oxide',
        'ocean \x1dfish meal': 'ocean fish meal'},
        'Cat Raw Food': {'         meal': '',
        '\\xa0': ' ',
        ';': '\\n',
        ' ,': ',',
        '*(official name is marine microalgae)': '',
        '\\u200b\u200btrout': ' ',
        '?': ' ',
        '\\uu202f': ' ',
        '\\t': ',',
        'a639120': '',
        ', preserved with mixed tocopherols and citric acid': ', preserved with mixed tocopherols, and citric acid',
        '>': '',
        '<': '',
        'trace': '',
        ' minerals': '',
        ' vitamins': '',
        ' b626618-13': '',
        'sa�ower oil': 'safflower oil',
        'boneless, skinless': 'boneless skinless',
        'sa\\x1dower oil': 'safflower oil',
        'dried bacillus coagulans, fermentation product.': 'dried bacillus coagulans fermentation product',
        ' +': ' ',
        '\\n': ' ',
        'sa\x1dower': 'safflower'},
        'Cat Wet Food': {'animal fat, (source of omega 6 fatty acids [preserved with bha/citric acid])': 'animal fat (preserved with citric acid)',
        'essential nutrients and other ingredients:': ',',
        '(filtered) water': 'water',
        'beef meat': 'beef',
        'chicken (boneless, skinless breast)': 'boneless skinless chicken breast',
        'duck (boneless, skinless, breast)': 'boneless skinless duck breast',
        'calcium iodate and sodium selenite': 'calcium iodate, sodium selenite',
        'carrots tomato concentrate': 'carrots, tomato concentrate',
        'chicken 76%': 'chicken',
        'potassium, chloride': 'potassium chloride',
        'choline chloride parsley.': 'choline chloride, parsley',
        'copper glycine, complex': 'copper glycine complex',
        'menadione sodium bisulfite, complex': 'menadione sodium bisulfite complex',
        'cranberries coconut.': 'cranberries, coconut',
        'fish oil (preserved with mixed tocopherols) dl-methionine': 'fish oil (preserved with mixed tocopherols), dl-methionine',
        'folic acid) inulin': 'folic acid), inulin',
        'folic acid. water added for processing': 'folic acid, water added for processing',
        'guar gum     sweet potatoes': 'guar gum, sweet potatoes',
        'icelandic fish (cod, haddock, pollock, monkfish, lumpfish, plaice)': 'icelandic fish',
        'manganese proteinate ethylenediamine dihydriodide': 'manganese proteinate, ethylenediamine dihydroiodide',
        'menadione, sodium': 'menadione sodium',
        'menhaden fish oil (preserved with mixed tocopherols) magnesium sulfate': 'menhaden fish oil (preserved with mixed tocopherols), magnesium sulfate',
        ', no carrageenan, no guar gum and no xanthan gum.': '',
        "pea starch\\xa0\xa0 brewer's dried yeast": "pea starch, brewer's dried yeast",
        'potassium iodide) calcium carbonate': 'potassium iodide, calcium carbonate',
        'potassium iodide) sodium carbonate': 'potassium iodide, sodium carbonate',
        'potassium iodide] xanthan gum': 'potassium iodide, xanthan gum',
        'potassium iodide)] xanthan gum': 'potassium iodide, xanthan gum',
        'preserved with mixed tocopherols. vitamin b5': 'vitamin b5',
        'pyfidoxine hydrochloride (vitamin b6)': 'pyridoxine hydrochloride (source of vitamin b6)',
        'rosemary extract. sodium selenite': 'sodium selenite',
        'salmon oil (preserved with mixed tocopherols) choline chloride': 'salmon oil (preserved with mixed tocopherols), choline chloride',
        'salmon oil (preserved with mixed tocopherols) potassium chloride': 'salmon oil (preserved with mixed tocopherols), potassium chloride',
        'sodium selenite) choline chloride': 'sodium selenite), choline chloride',
        'sodium selenite manganese proteinate': 'sodium selenite, manganese proteinate',
        'sodium selenite riboflavin supplement': 'sodium selenite, riboflavin supplement',
        'vitamin  d3, supplement': 'vitamin  d3 supplement',
        'vitamin a supplement biotin vitamin d3 supplement': 'vitamin a supplement, biotin, vitamin d3 supplement',
        'vitamin b12 supplement manganese proteinate': 'vitamin b12 supplement, manganese proteinate',
        'vitamin b12 supplement. menadione sodium bisulfite': 'vitamin b12 supplement, menadione sodium bisulfite',
        'vitamin b12. calcium iodate': 'vitamin b12, calcium iodate',
        'vitamin d3 supplement) inulin': 'vitamin d3 supplement), inulin',
        'vitamin d3 supplement) blueberries': 'vitamin d3 supplement), blueberries',
        'water sufficient for processing 24%': 'water sufficient for processing',
        'water sufficient forprocessing': 'water sufficient for processing',
        'postassium': 'potassium',
        'sunflower oi,': 'sunflower oil,',
        '         meal': '',
        '\\xa0': ' ',
        ', (': ' (',
        ' ,': ',',
        '*(official name is marine microalgae)': '',
        '\u200b\\u200btrout': ' ',
        '?': ' ',
        '\\u202f': ' ',
        '\\t': ',',
        'a639120': '',
        '. b470920-5': '',
        ' minerals': ',',
        ' vitamins': ',',
        ' b626618-13': '',
        ':': '',
        '"': '',
        'processing.': 'processing,',
        ' +': ' ',
        '\\n\\n': '\\n',
        'riboflavin supplement vitamin,': 'riboflavin supplement, vitamin',
        'vitamin e, a, d3, b12 supplements,': 'vitamin e, vitamin a, vitamin d3, vitamin b12,',
        'folic acid inulin': 'folic acid, inulin',
        '(boneless, skinless breast)': '',
        '�': '',
        'ingredients': '',
        '\\n': ' ',
        ',,': ',',
        '[': '',
        ']': '',
        '))': ')',
        ') water sufficient for processing': '), water sufficient for processing',
        '}': '',
        '{': '',
        'minerals': '',
        'vitamins': '',
        '). (': ',',
        ') (': ',',
        'guar gum (zinc oxide': 'guar gum, zinc oxide',
        "pea starch brewer's dried yeast": "pea starch, brewer's dried yeast",
        'taurine (vitamin e supplement': 'taurine, vitamin e supplement'},
        'Dog Veterinary Diet': {'new:': '',
        '         meal': '',
        '��': ' ',
        ';': '\n',
        ' ,': ',',
        '*(official name is marine microalgae)': '',
        '���trout': ' ',
        '?': ' ',
        '���': ' ',
        '\t': ',',
        'a639120': '',
        ', preserved with mixed tocopherols and citric acid': ', preserved with mixed tocopherols, and citric acid',
        ' minerals': '',
        ' vitamins': '',
        ' b626618-13': '',
        '15% - a source of fiber': '',
        '<': '',
        '>': '',
        '(, )': ',',
        '*': '',
        'niacin, (vitamin b-3)': 'niacin (vitamin b-3)',
        '. d-2620.': '',
        'trace zinc proteinate': 'zinc proteinate',
        'minerals magnesium oxide': 'magnesium oxide',
        'dried bacillus coagulans, fermentation product.': 'dried bacillus coagulans fermentation product',
        ' +': ' ',
        "r'\n+": '\n',
        'ingredients': '',
        '\n': ''},
        'Dog Raw Food': {'         meal': '',
        '\\xa0': ' ',
        ';': '\\n',
        ' ,': ',',
        '*(official name is marine microalgae)': '',
        '\\u200btrout': ' ',
        '?': ' ',
        '\\u202f': ' ',
        '\\t': ',',
        'a639120': '',
        ', preserved with mixed tocopherols and citric acid': ', preserved with mixed tocopherols, and citric acid',
        'vitamins & minerals': '',
        ' minerals': '',
        ' vitamins': '',
        ' b626618-13': '',
        '<': '',
        '>': '',
        '(, )': ',',
        '*': '',
        'ingredients': '',
        'sa�ower oil': 'safflower oil',
        'bonless, skinless': 'boneless skinless',
        'contains a source of live (viable) naturally occurring microorganisms': '',
        'contains a source of live naturally occuring microorganisms': '',
        '\\n': '',
        'delivered fresh or raw': '',
        'chicken including ground chicken bone': 'chicken, ground chicken bone',
        'pea deboned salmon': 'pea, deboned salmon',
        'passionflower': 'passion flower',
        'freeze-dried duck': 'freeze-dried duck',
        'dried bacillus coagulans fermentation product zinc proteinate': 'dried bacillus coagulans fermentation product, zinc proteinate',
        'dried chicory root (source of inulin) dried pediococcus acidilactici fermentation product': 'dried chicory root (source of inulin), dried pediococcus acidilactici fermentation product',
        'omega 3 & 6 from fish oil': 'omega 3 & 6 from fish oil',
        'dried bacillus coagulans, fermentation product.': 'dried bacillus coagulans fermentation product',
        '(proteinated and)': '',
        'potassium, chloride': 'potassium chloride'},
        'Cat Veterinary Diet': {'         meal': '',
        '\\xa0': ' ',
        ';': '\\n',
        ' ,': ',',
        '*(official name is marine microalgae)': '',
        '\\u200b\u200btrout': ' ',
        '?': ' ',
        '\\u202f': ' ',
        '\\t': ',',
        'a639120': '',
        ', preserved with mixed tocopherols and citric acid': ', preserved with mixed tocopherols, and citric acid',
        '>': '',
        '<': '',
        'trace': '',
        ' minerals': '',
        ' vitamins': '',
        ' b626618-13': '',
        'sa�ower oil': 'safflower oil',
        'boneless, skinless': 'boneless skinless',
        'dried bacillus coagulans, fermentation product.': 'dried bacillus coagulans fermentation product',
        '\\n\\n': '\\n',
        '(l-ascorbyl-2-polyphosphate (source of vitamin c)': 'l-ascorbyl-2-polyphosphate'}}


# Another dictionary used for replacing noises in the ingredient panel for cleaning purposes.  
replace_dict = {'maize':"corn",
                "brewers'":"brewers",
        '). (': ', ',
        ') (': ', ',
        'taurine (vitamin': 'taurine, vitamin',
#                 'chicken- and turkey meal (chicken 8%, total poultry 13%)':'chicken and turkey meal',
        'choline chloride (iron amino acid chelate': 'choline chloride, iron amino acid chelate',
        'natural flavor (zinc oxide': 'natural flavor, zinc oxide',
        "pea starch brewer's dried yeast": "pea starch, brewer's dried yeast",
        'organic sage (zinc amino acid complex': 'organic sage, zinc amino acid complex',
        ': (': ' ',
        'bisul te': 'bisulfate',
        'sa ower oil': 'safflower oil',
        'potassium iodide beta-carotene': 'potassium iodide, beta-carotene',
        '[': '',
        ']': '',
        '{': '',
        '}': '',
        '(proteinated and )': '',
        'rosemary.': 'rosemary',
        'iron amino acid chelate vitamin e supplement': 'iron amino acid chelate, vitamin e supplement',
        'dried trichoderma longibrachiatum fermentation extract.': 'dried trichoderma longibrachiatum fermentation extract',
        'dried lactobacillus casei fermentation product.': 'dried lactobacillus casei fermentation product',
        'dried bacillus coagulans fermentation product zinc proteinate': 'dried bacillus coagulans fermentation product, zinc proteinate',
        'salt  choline chloride': 'salt, choline chloride',
        'turkey & bacon turkey': 'turkey, bacon, turkey',
        'calcium iodate) taurine': 'calcium iodate, taurine',
        'dicalcium phosphate  iron proteinate': 'dicalcium phosphate, iron proteinate',
        'turkey & duck chicken': 'turkey, duck, chicken',
        '& calcium carbonate': ', calcium carbonate',
        'l-ascorbyl-2-polyphosphate (source of vitamin c) ferrous sulfate': 'l-ascorbyl-2-polyphosphate (source of vitamin c), ferrous sulfate',
        'vitamin b12 supplement) guar gum': 'vitamin b12 supplement, guar gum',
        'carbon dioxide) peas': 'carbon dioxide, peas',
        'milk ingredients': 'milk',
        'folic acid) xanthan gum': 'folic acid, xanthan gum',
        '\u200btrout': 'trout',
        'pea deboned salmon': 'pea, deboned salmon',
        'laucine': 'leucine',
        'wild-caught yellowfin tuna & wild-caught shrimp': 'wild-caught yellowfin tuna, wild-caught shrimp',
        '_x0003_': '',
        'chicken (including ground chicken bone, source of glucosamine and chondroitin sulfate)': 'chicken (including ground chicken bone-source of glucosamine and chondroitin sulfate)',
        
        'boneless/skinless salmon water sufficient for processing rice (salt calcium carbonate monodicalcium phosphate choline chloride potassium chloride zinc proteinate iron proteinate, copper proteinate manganese proteinate calcium iodate': 'boneless/skinless salmon, water sufficient for processing, rice, salt,, calcium carbonate, monodicalcium phosphate, choline chloride, potassium chloride, zinc proteinate, iron proteinate, copper proteinate, manganese proteinate, calcium iodate',
        
        'potassium chloride, vitamin e supplement': 'potassium chloride, vitamin e supplement',
        
        'vitamin e supplement niacin vitamin a supplement thiamine mononitrate riboflavin': 'vitamin e supplement, niacin, vitamin a supplement, thiamine mononitrate, riboflavin',
        
        'biotin vitamin b12 supplement folic acid vitamin d3 supplement d-calcium pantothenate) taurine kale blueberries raspberries cranberries carrots': 'biotin, vitamin b12 supplement, folic acid, vitamin d3 supplement, d-calcium pantothenate, taurine, kale, blueberries, raspberries, cranberries, carrots',
        
        'boneless turkey water sufficient for processing rice (salt calcium carbonate monodicalcium phosphate choline chloride potassium chloride zinc proteinate iron proteinate': 'boneless turkey, water sufficient for processing, rice, salt, calcium carbonate, monodicalcium phosphate, choline chloride, potassium chloride, zinc proteinate, iron proteinate',
    
    
        'copper proteinate manganese proteinate calcium iodate': 'copper proteinate, manganese proteinate, calcium iodate',
        
        'folic acid). magnesium sulfate': 'folic acid, magnesium sulfate',
        
        'potassium chloride (vitamin e supplement': 'potassium chloride, vitamin e supplement',
        
        'copper proteinate manganese proteinate calcium iodate': 'copper proteinate, manganese proteinate, calcium iodate',
        
        'flaxseed and trace elements. total vegetables (1%).': 'flaxseed, trace, vegetables (1%)',
        
        'carrageenan.': 'carrageenan',
        'carrageenan e466620': 'carrageenan',
        'sodium selenite. potassium iodide)': 'sodium selenite, potassium iodide',
        'zinc oxide. manganese sulfate. copper glycine complex': 'zinc oxide, manganese sulfate, copper glycine complex',
        'biotin) carrageenan': 'biotin, carrageenan',
        'biotin) taurine': 'biotin, taurine',
        'copper, sulfate,': 'copper sulfate,',
        'acid balance ® (phosphoric acid': 'phosphoric acid',
        ', d (zinc sulfate,': ', zinc sulfate,',
        'nvgen ® (yeast extract,': 'yeast extract,',
        'copper glycine complex. sodium selenite': 'copper glycine complex, sodium selenite',
        
        'crab surimi (ocean whitefish, crab broth)': 'crab surimi (ocean whitefish crab broth)',
        
        'd-calcium pantothenate. riboflavin supplement': 'd-calcium pantothenate, riboflavin supplement',
        'fructooligosaccharides. calcium sulfate': 'fructooligosaccharides, calcium sulfate',
        'boneless/skinless salmon water sufficient for processing rice (salt calcium carbonate monodicalcium phosphate choline chloride potassium chloride zinc proteinate iron proteinate copper proteinate': 'boneless/skinless salmon, water sufficient for processing, rice, salt, calcium carbonate, monodicalcium phosphate, choline chloride, potassium chloride, zinc proteinate, iron proteinate, copper proteinate',
        'apple cider vinegar choline chloride': 'apple cider vinegar, choline chloride',
        'menadione sodium bisulfite complex (source of vitamin k activity) folic acid': 'menadione sodium bisulfite complex (source of vitamin k activity), folic acid',
        
        'rice starch, digest,, ': 'rice starch,',        
        'riboflavin biotin': 'riboflavin, biotin',        
        'vitamin d-3 supplement. c470822-5': 'vitamin d-3 supplement,',        
        '. x000d': '',        
        'vitamin d-3 supplement. c471022-5': 'vitamin d-3 supplement,',        
        'biotin). magnesium sulfate': 'biotin, magnesium sulfate',        
        'sodium selenite) sodium carbonate': 'sodium selenite, sodium carbonate',
        
        'vitamin d (vitamin d3 supplement)': 'vitamin d, vitamin d3 supplement',
        'vitamin d-3 supplement d427622': 'vitamin d-3 supplement',
        
        "lamb meal oatmeal brown rice chicken fat (preserved with mixed tocopherols) tomato pomace brewer's yeast threonine potassium chloride dl methionine taurine calcium propionate blueberries raspberries cranberries (zinc proteinate iron proteinate calcium carbonate manganese proteinate copper proteinate selenium yeast calcium iodate": "lamb meal, oatmeal, brown rice, chicken fat (preserved with mixed tocopherols), tomato pomace, brewer's yeast, threonine, potassium chloride, dl methionine, taurine, calcium propionate, blueberries, raspberries, cranberries, zinc proteinate, iron proteinate, calcium carbonate, manganese proteinate, copper proteinate, selenium yeast, calcium iodate",
        
        "duck meal burbank potato norkotah potato pumpkin chicken fat (preserved with mixed tocopherols) brewer's dried yeast potassium chloride choline chloride dl methionine blueberries raspberries cranberries threonine calcium propionate taurine  zinc proteinate iron proteinate calcium carbonate manganese proteinate copper proteinate selenium yeast calcium iodate) :(vitamin e supplement niacin thiamine mononitrate vitamin a supplement d-calcium pantothenate riboflavin pyridoxine hydrochloride biotin vitamin b12 supplement vitamin d3 supplement folic acid) rosemary extract": "duck meal, burbank potato, norkotah potato, pumpkin, chicken fat (preserved with mixed tocopherols), brewer's dried yeast, potassium chloride, choline chloride, dl methionine, blueberries, raspberries, cranberries, threonine, calcium propionate, taurine,  zinc proteinate, iron proteinate, calcium carbonate, manganese proteinate, copper proteinate, selenium yeast, calcium iodate, vitamin e supplement, niacin, thiamine mononitrate, vitamin a supplement, d-calcium pantothenate, riboflavin, pyridoxine hydrochloride, biotin, vitamin b12 supplement, vitamin d3 supplement, folic acid, rosemary extract",
        
        
        "vitamin e supplement niacin thiamine mononitrate d-pantothenic acid vitamin a supplement riboflavin pyridoxine hydrochloride biotin vitamin b12 supplement vitamin d3 supplement folic acid ) glucosamine hydrochloride": "vitamin e supplement, niacin, thiamine mononitrate, d-pantothenic acid, vitamin a supplement, riboflavin, pyridoxine hydrochloride, biotin, vitamin b12 supplement, vitamin d3 supplement, folic acid, glucosamine hydrochloride",
        
        "ocean fish meal oatmeal brown rice chicken fat (preserved with mixed tocopherols) lamb meal tomato pomace brewer's dried yeast potassium chloride dicalcium phosphate choline chloride blueberries raspberries cranberries calcium propionate  zinc proteinate iron proteinate calcium carbonate manganese proteinate copper proteinate selenium yeast calcium iodate)  vitamin e supplement niacin thiamine mononitrate d-pantothenic acid vitamin a supplement riboflavin pyridoxine hydrochloride biotin vitamin b12 supplement vitamin d3 supplement folic acid) rosemary extract": "ocean fish meal, oatmeal, brown rice, chicken fat (preserved with mixed tocopherols), lamb meal, tomato pomace, brewer's dried yeast, potassium chloride, dicalcium phosphate, choline chloride, blueberries, raspberries, cranberries, calcium propionate,  zinc proteinate, iron proteinate, calcium carbonate, manganese proteinate, copper proteinate, selenium yeast, calcium iodate,  vitamin e supplement, niacin, thiamine mononitrate, d-pantothenic acid, vitamin a supplement, riboflavin, pyridoxine hydrochloride, biotin, vitamin b12 supplement, vitamin d3 supplement, folic acid, rosemary extract",
        
        'apples blueberries': 'apples, blueberries',
        '(vitamin a, acetate': '(vitamin a acetate',
        'and vitamin e supplement': 'vitamin e supplement',
        'chondroitin sulfate natural preservative (natural mixed tocopherols': 'chondroitin sulfate, natural preservative, natural mixed tocopherols',
        'manganese, proteinate,': 'manganese proteinate,',
        '. store in a cool, dry place': '',
        'l-carnitine d-calcium pantothenate (vitamin b5)': 'l-carnitine, d-calcium pantothenate (vitamin b5)',
        'mixed tocopherols (a source of vitamin e) and rosemary extract': 'mixed tocopherols (a source of vitamin e), rosemary extract',
        'natural flavor potassium chloride': 'natural flavor, potassium chloride',
        
        'calorie content me (calculated) = 3790 kcal/kg': '',
        '. contains a source of live (viable) naturally occurring microorganisms': '',
        'sodium selenite we use chelated': 'chelated sodium selenite',
        'rosemary extract.thiamine mononitrate': 'rosemary extract, thiamine mononitrate',
        'dried saccharomyces, cerevisiae fermentation extract': 'dried saccharomyces cerevisiae fermentation extract',
        'glucosamine, hydrochloride,': 'glucosamine hydrochloride,',
        'dried b. animalis fermentation product and dried l. reuteri fermentation product': 'dried bifidobacterium animalis fermentation product, dried lactobacillus reuteri fermentation product',
        
        'dried lactobacillus, platarum fermentation product': 'dried lactobacillus platarum fermentation product',
        'dried rhizopus oryzae fermentation, extract': 'dried rhizopus oryzae fermentation extract',
        'rosemary extract and spearmint extract': 'rosemary extract, spearmint extract',
        'dried whey. dried blueberries': 'dried whey, dried blueberries',
        'copper amino acid complex) choline chloride': 'copper amino acid complex, choline chloride',
        '430 kcal/cup': '',
        'citric acid, (preservative)': 'citric acid (preservative)',
        'thiamine mononitrate, (vitamin b1)': 'thiamine mononitrate (vitamin b1)',
        'citric acid, (preservative)': 'citric acid (preservative)',
        'chicken fat (preserved with mixed tocopherols, a source of natural vitamin e)': 'chicken fat (preserved with mixed tocopherols source of vitamin e)',
        'riboflavin supplement, (source of vitamin b2)': 'riboflavin supplement (source of vitamin b2)',
    
    
        'dried cranberries l-lysine': 'dried cranberries, l-lysine',
        'chicken fat (preserved with mixed tocopherols, form of vitamin e)': 'chicken fat (preserved with mixed tocopherols and form of vitamin e)',
        'salmon oil, (preserved with mixed tocopherols, form of vitamin e)': 'salmon oil (preserved with mixed tocopherols)',
        'salmon oil (preserved with mixed tocopherols, source of vitamin e)': 'salmon oil (preserved with mixed tocopherols)',
        'chicken fat (preserved with mixed tocopherols, form of vitamin e)': 'chicken fat (preserved with mixed tocopherols)',
        'chicken fat (preserved with mixed tocopherols, source of vitamin e)': 'chicken fat (preserved with mixed tocopherols)',
        'chicken fat (preserved with mixed tocopherols, soruce of vitamin e)': 'chicken fat (preserved with mixed tocopherols)',
        
        'thiamine, mononitrate': 'thiamine mononitrate',        
        'dry place': '',        
        'fruits and vegetables (carrots': 'carrots',
        ', d-calcium, pantothenate': ', d-calcium pantothenate',
        'fruits and vegetables (carrots': 'carrots',
    }


description_dictionary = {'Supplement': 'Acceptable Quality: Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers.',
 'Others': 'Poor Quality: Undefined category; ingredients should be transparent and recognizable.',
 'Organ Parts': 'Acceptable Quality: Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A.',
 'Fish Meats': 'Acceptable Quality: High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury).',
 'Seafoods': 'Acceptable Quality: Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important.',
 'Whole Meats': 'Acceptable Quality: Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food.',
 'Natural Additives': 'Acceptable Quality: When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals).',
 'Artificial Colors': 'Poor Quality: Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs.',
 'Legumes': 'Poor Quality: Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets.',
 'Algae': 'Acceptable Quality: Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination.',
 'Meat Meals': 'Poor Quality: Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability.',
 'Animal Fat': 'Acceptable Quality: Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality.',
 'Plant Based Fat': 'Acceptable Quality: Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly.',
 'Nuts': 'Poor Quality: Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain.',
 'Natural Preservatives': 'Acceptable Quality: Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract.',
 'Enzymes & Probiotics': 'Acceptable Quality: Promotes digestive health and nutrient absorption, contributing to overall gut health.',
 'Natural Flavors': 'Poor Quality: "Natural" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable.',
 'Animal Digest': 'Poor Quality: Highly processed and often sourced from unnamed animals, making it an undesirable flavor enhancer with low nutritional value.',
 'Blood & Plasma': 'Poor Quality: Low-quality, heavily processed by-products used to increase protein content cheaply. Unnecessary in high-quality diets.',
 'Natural Colors': 'Acceptable Quality: Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food.',
 'Fruits & Vegetables': 'Acceptable Quality: Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health.',
 'Roughages': 'Acceptable Quality: Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains.',
 'Meat Broths': 'Poor Quality: Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings.',
 'Artificial Flavors': 'Poor Quality: Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs.',
 'Artificial Preservatives': 'Poor Quality: Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin.',
 'Barley': 'Acceptable Quality: Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient.',
 'Brewers Products': 'Poor Quality: Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value.',
 'Meats': 'Acceptable Quality: Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient.',
 'Meat By-Products': 'Poor Quality: Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious.',
 'Meat Isolates or Powder': 'Poor Quality: Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats.',
 'Dairy Products': 'Poor Quality: Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included.',
 'Rice': 'Acceptable Quality: Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs.',
 'Artificial Additives': 'Poor Quality: Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies.',
 'Wheat, Corn, Soy': 'Poor Quality: Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset.',
 'Oilseed Meals': 'Poor Quality: Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable.',
 'Human Food Ingredients': 'Acceptable Quality: As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key.',
 'Chia': 'Acceptable Quality: Rich in omega-3s, fiber, and antioxidants, chia seeds are a good addition in moderation for coat health and digestion.',
 'Dried Meats': 'Acceptable Quality: Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source.',
 'Peas': 'Poor Quality: Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets.',
 'Grain Meals': 'Poor Quality: Highly processed and of lower nutritional value than whole grains. Often used as fillers.',
 'Oilseeds': 'Acceptable Quality: Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants.',
 'Sorghum': 'Acceptable Quality: Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins.',
 'Oats': 'Acceptable Quality: Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn.',
 'Quinoa': 'Acceptable Quality: A good source of protein and amino acids but should not be a primary ingredient. Can be used as an alternative to grains for some dogs.',
 'Rye': 'Poor Quality: Can be hard for dogs to digest and is less nutritionally valuable compared to other grains like oats or rice. May cause digestive upset.'}


# Dictionary specifying the CO2 emissions in percentile of each ingredient subcategory.
# This dictionary is used to calculate the CO2 emissions of the top 5 ingredients in the ingredient panel based on their subcategory.
emission_dict = {'algae': 39.56,
 'animal fat': 60.33,
 'artificial additives': 29.87,
 'artificial preservatives': 29.87,
 'barley': 12.97,
 'beef': 88.03,
 'beef and chicken': 77.54,
 'beef fat': 88.03,
 'beet fiber': 35.85,
 'bison': 88.03,
 'boar': 80.19,
 'borage': 25.0,
 'brazilian nut': 10.38,
 'bread': 37.74,
 'brewers products': 32.08,
 'buckwheat': 44.88,
 'buffalo': 88.03,
 'butter': 5.66,
 'canola': 25.94,
 'canola oil': 25.94,
 'cellulose products': 0.47,
 'cheese': 70.13,
 'chia': 11.32,
 'chicken': 67.05,
 'chicken and beef': 77.54,
 'chicken and lamb': 76.16,
 'chicken and salmon': 69.19,
 'chicken and turkey': 66.70,
 'chicken fat': 0.47,
 'coconut': 13.92,
 'coconut oil': 25.94,
 'collagen': 99.53,
 'corn': 14.15,
 'corn oil': 17.45,
 'duck': 49.53,
 'duck fat': 49.53,
 'egg': 56.13,
 'faba': 24.06,
 'farro': 17.45,
 'fish': 71.32,
 'fish oil': 0.47,
 'flaxseed': 13.68,
 'flaxseed oil': 25.94,
 'fruits': 35.57,
 'garbanzo': 24.06,
 'gelatin': 99.53,
 'general animal products': 91.27,
 'general legume products': 30.66,
 'goat': 85.28,
 'goose': 49.53,
 'grass': 50.94,
 'guinea': 44.02,
 'ham': 72.33,
 'herbs': 50.94,
 'kangaroo': 44.02,
 'lamb': 85.28,
 'lamb and chicken': 76.16,
 'lamb fat': 85.28,
 'lentils': 24.06,
 'macaroni': 44.88,
 'maize':14.15,
 'milk': 34.12,
 'minerals': 29.87,
 'mung': 24.06,
 'natural additives': 29.87,
 'natural flavors': 70.28,
 'natural preservatives': 29.87,
 'oat fiber': 56.72,
 'oats': 56.72,
 'olive oil': 24.06,
 'ostrich': 63.68,
 'other seafood': 88.92,
 'pasta': 44.88,
 'pea fiber': 89.62,
 'peanut butter': 19.34,
 'pork': 72.33,
 'pork fat': 72.33,
 'quinoa': 12.74,
 'rabbit': 66.51,
 'rice': 31.47,
 'sesame oil': 25.94,
 'sorghum': 9.67,
 'soy fiber': 20.28,
 'soybean': 35.97,
 'soybean oil': 25.0,
 'spaghetti': 37.74,
 'spices': 50.94,
 'sugarcane fiber': 0.47,
 'sunflower': 11.79,
 'sunflower oil': 17.45,
 'sunflower seed': 6.13,
 'tapioca/cassava products': 39.56,
 'tea': 50.94,
 'turkey': 66.35,
 'turkey fat': 66.35,
 'unknown': 8.81,
 'vegetable oil': 24.06,
 'vegetables': 39.56,
 'venison': 44.02,
 'vitamins': 29.87,
 'wheat': 44.88,
 'yeast': 0.47,
 'yogurt': 47.17}

ingredient_dictionary = {
"(amino acids) tryptophan": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"(dl-alpha tocopherol acetate (source of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"(ferrous sulfate (source of iron)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"(filtered) water sufficient for processing": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"(l-ascorbyl-2-poylyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"(thiamine mononitrate (vitamin b-1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"(vitamin e supplement)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"100% pure beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure chicken breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure duck liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure lamb liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure ocean-caught human grade minnow": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"100% pure ocean-caught human grade yellowfin tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"100% pure pork liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure turkey liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made chicken breast & organic catnip": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made human grade beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made human grade beef liver and wisconsin cheddar cheese": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made human grade chicken breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made human grade chicken breast & duck liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made human grade chicken breast & new-zealand lamb liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made human grade duck liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure usa sourced & made human grade turkey breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"100% pure wild-caught & made in the usa human grade sockeye salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"100% pure wild-caught & made in usa human grade pacific ocean whitefish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"100% pure wild-caught & made in usa human grade shrimp": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"100% pure wild-caught human grade sockeye salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"100% whole beef cooked in its own juices": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"a monosaccharide complex l-rhamnose": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"a -tocopherol acetate (source of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"acadian redfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"passion flower": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"yellow squash": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"acorn squash": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"added color": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"added color (red 3 and other artificial color)": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"added color (red 3 and other color)": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"added color fd&c red #40": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"added color red #40": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"added colors": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"aflalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"agar agar": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"agar-agar": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"ahi tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"alaska pollock meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"alaskan cod meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"alaskan pollock oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"alfalfa": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"alfalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"alfalfa nutrient concentrate": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"algae": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"algae fat extract": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"alligator": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"alligator meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"almond oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"almonds": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"aloe vera": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"aloe vera extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"aloe vera gel concentrate": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"aloe verra": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"alpha-tocopherol acetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"alpha-tocopherol acetate (source of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"alpha-tocopherol acetate (vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"althea root": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"amino acids (l-lysine monohydrochloride)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"amino acids l-lysine monohydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"anchovies": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"anchovies 5%": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"anchovy": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"anchovy & sardine meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"anchovy and sardine meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"anchovy meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"anchovy meal (natural source of chondroitin and glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"and citric acid": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"and citric acid (preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"and dried l. reuteri fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"and fd&c blue #1": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"and green beans ": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"and other added color": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"and potassium iodide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"and rosemary extract": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"and spearmint": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"and spearmint extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"angus beef flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural angus beef flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"animal digest": {
"Type": "Animal Digest",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often sourced from unnamed animals, making it an undesirable flavor enhancer with low nutritional value."
},
"animal digest (source of chicken flavor)": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"animal digest (source of liver flavor)": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"animal digest (source of roasted flavor)": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"animal fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (bha used as a preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (bha used as preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (preserved with bha & citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (preserved with bha and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (preserved with mixed tocopherols and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (preserved with tbhq and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids preserved with bha & citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids preserved with bha/citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids) preserved with bha/citric acid": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids preserved with bha and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids (preserved with bha & citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids (preserved with bha & citric acid))": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids (preserved with bha and citric acid))": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids (preserved with bha/citric acid))": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids) (preserved with bha/citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acidspreserved with bha & citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat (source of omega 6 fatty acids) preserved with bha & citric acid": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat preserved with mixed tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat preserved with mixed tocopherols and citric acid": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat preserved with mixed-tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fat preserved with mixed-tocopherols (form of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal fats": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"animal liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"animal liver flavor": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"animal plasma": {
"Type": "Blood & Plasma",
"Quality": "Poor Quality",
"Quality Description": "Low-quality, heavily processed by-products used to increase protein content cheaply. Unnecessary in high-quality diets."
},
"annatto (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"annatto color": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"annatto extract (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"apple": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"apple cide vinegar": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"apple cider vinegar": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"apple fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"apple pectin": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"apple pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"apple powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"apple puree": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"apples": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"apricots": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"arctic char": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"artichokes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"artificial and fish broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"artificial and natural flavors": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"artificial beef flavor": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"ascorbic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ascorbic acid (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"ascorbic acid (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ascorbic acid source ofvitamin c": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ascorbic acid (vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ascorbic acid [source of vitamin c]": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ascorbic acid source of vitamin c": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"asparagus": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"aspergillus oryzae fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"atlantic tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"a-tocopherol acetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"a-tocopherol acetate (source of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"a-tocopherolacetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"avocado": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"avocado meal": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"avocado oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"avocado oil (source of omega 3)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"b-12 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"baby clam": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"bacillus licheniformis": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bacillus subtilis": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bacon": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"bacon broth (source of bacon flavor)": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"bacon fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"bacon flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"bacterial culture": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bamboo fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"banana": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"banana powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"bananas": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"barley grass": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"barley grass extract": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"barley malt": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"barramundi": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"bartlett pears": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"basa": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"basil": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"bay leaves": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"bbq chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"beef": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"beef & bone meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"beef (source of glucosamine)": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"beef (with ground bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef and bone meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"beef and chicken broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"beef blood": {
"Type": "Blood & Plasma",
"Quality": "Poor Quality",
"Quality Description": "Low-quality, heavily processed by-products used to increase protein content cheaply. Unnecessary in high-quality diets."
},
"beef bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef bone broth": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"beef by-product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"beef by-products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"beef cartilage": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef fat (preserved with mixed tocopherols and ascorbic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef fat naturally preserved with mixed-tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef fat naturally preserved with vitamin e": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef fat preserved with mixed-tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef 5%": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"beef hearts": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef kidneys": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"grass fed beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef lung": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef lungs": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"beef meal (preserved with mixed tocopherols)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"beef meal (source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"beef meal (source of glucosamine and chondroitin)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"beef meal (source of methionine-cystine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"beef organ": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef organs": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef pizzle": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef protein": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"beef spleen": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef spleens": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef stock": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef stomach": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beef tallow": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef tallow (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef tallow naturally preserved with mixed-tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef tallow preserved with mixed-tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"beef tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beefhide": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"beet": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"beet fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"beet greens": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"beet juice (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"beet powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"beet pulp": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"beets": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"beta carotene": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"beta carotene (preserved with mixed tocopherols)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"beta carotene (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"beta-carotein": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"beta-carotene": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"beta-carotene (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"betaine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"betaine anhydrous": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"betaine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"bha": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"bha (a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"bha (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"bha (used as a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"bha (used as preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"bifido bacterium bifidium fermentation product (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bifido bacterium bifidum fermentation product dehydrated": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bifidobacterium animalis": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bifidobacterium animalis product dehydrated": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bifidobacterium bifidum": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bifidobacterium thermophilum": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bifidobacterium thermophilum fermentation product dehydrated": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bioena": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"biotin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"biotin ": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"biotin (vitamin b7)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"biotin (vitamin b-7)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"biotin (vitamin b8)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"biotin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"biotin supplement (vitamin b7)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"biotin vitamin b-7": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"biotin(vitamin b7)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"bisglycinate chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"bison": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"bison meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"bison tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"bison/buffalo": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"bitamin b12 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"bitter orange peel": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"black beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"black peper": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"black pepper": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"blackberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"blood meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"blood meal conventionally dried": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"blue #2": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"blue 1": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"blue 2": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"blue 2 lake": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"blue whiting meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"hydrolyzed blue whiting": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"blueberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"blueberry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"blueberry fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"blueberry powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"boar": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"boar broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"boar liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"boar meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"boar meat": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"bok choy": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"bone meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"boneless & skinless chicken breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"boneless beef": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"boneless chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"boneless pork shoulder": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"boneless skinless chicken breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"boneless skinless duck breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"boneless turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"boneless/skinless salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"bonita tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"bonito": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"bovine colostrum": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"braised rib flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"bream": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"brewer\u2019s dried yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"brewer\u2019s rice": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"brewer\u2019s yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"brewer's dried east": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"brewers dried yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"brewer's dried yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"brewer's liquid yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"brewers rice": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"brewer's rice": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"brewers rice flour": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"brewers yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"brewer's yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"broccoli": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"broccoli sprouts": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"brocoli": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"brown kelp": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"brown rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"brown rice flour": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"brown sugar": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"brussels sprouts": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"buckwheat": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"buffalo": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"buffalo broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"buffalo meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"burbank potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"butternut squash": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"button mushrooms": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cabbage": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"caciumiodate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calamari": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"calamari broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"calamari consomm\u00e9": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"calci um sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium carbon": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"& calcium carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium citrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium d-pantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium d-pantothenate (source of vitamin b5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium gluconate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium iodate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium iodate mixed tocopherols": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium lactate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium lodate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium panthotenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium panthothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b5 (calcium pantothenate)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothenate source of vitamin b5": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium panthothenate (vitamin b5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantohtenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothenate vitamin b-5": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothenate (source of vitamin b5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothenate (vitamin b5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothenate (vitamin b-5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothenate (vitaminb5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothenate(vitamin b5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium pantothnate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium propionate": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"calcium propionate (a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"calcium propionate (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"calcium stearate": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"magnesium stearate": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"calcium sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calcium sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calciumcarbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calciumiodate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calciumoxidate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calciumpantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"calciumsulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"camelia": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"camellia": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cane molasses": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"canola meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"canola oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (mixed tocopherols used as a preservative)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (preserved with mixed tocopherols & citric acid)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (preserved with mixed tocopherols- a source of vitamin e)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (preserved with mixed tocopherols and citric acid)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (preserved with mixed tocopherols source of vitamin e)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (preserved with mixed tocopherols-a source of vitamin e)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (source of omega 3 fatty acids)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (source of omega 6 fatty acids)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil from canola plants (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil preserved with mixed tocopherols": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil(preserved with rosemary extract)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canola oil (preserved with rosemary extract)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"canolaoil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"cantaloupe": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"canthaxanthin (color preserved with ethoxyquin)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"canthaxanthin": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"canthaxanthin (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"carageenan": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"caramel": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"caramel (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"caramel color": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"carbon dioxide": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"cardamom": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"carmine (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"carob": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"carob bean gum": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"carob gum": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"carotene": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"carrageenan": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"carrageenen": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"carrgeenan": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"carrot": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"carrot flakes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"carrot juice": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"carrot powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"carrot puree": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"carrots": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"casein": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"casia gum": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"cassava flour": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"cassava root": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"cassava root flour": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"cassava/tapioca": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"cassia gum": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"catfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"catfish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"catfish oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"catfish oil (preserved with mixed tocopherols and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"catfish oil preserved with mixed tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"cauliflower": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"caviar": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"cayenne": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"celery": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"celery extract": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"celery powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"celery root powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cellulase & hemicellulase": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"cellulase (trichoderma reesei)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"cellulose": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"cellulose fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"cellulose gum": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"cellulose powder": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"chamomile": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"chamomille": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"cheddar cheese": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"cheese": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"cheese (parmigiano reggiano)": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"cheese (source of cheddar cheese)": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"cheese 5%": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"cheese 6%": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"cheese meal": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"cheese powder (source of cheddar cheese flavor)": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"chelated zinc sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"chia": {
"Type": "Chia",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in omega-3s, fiber, and antioxidants, chia seeds are a good addition in moderation for coat health and digestion."
},
"chia seed": {
"Type": "Chia",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in omega-3s, fiber, and antioxidants, chia seeds are a good addition in moderation for coat health and digestion."
},
"chia seed oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"chia seeds": {
"Type": "Chia",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in omega-3s, fiber, and antioxidants, chia seeds are a good addition in moderation for coat health and digestion."
},
"chick pea": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"chick peas": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken 60%": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken drumstick 60%": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken 55%": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken (drumette)": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken (ground with bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken including ground chicken bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken (including ground chicken bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken (including ground chicken bone-source of glucosamine and chondroitin sulfate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken (natural source of chondroitin sulfate)": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken (source of glucosamine & chondroitin sulfate)": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken (source of glucosamine and chondroitin sulfate)": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken meal (source of glucosamine and chondroitin suflate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken (source of glucosamine)": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken (with ground bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken and beef broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"chicken and lamb broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"chicken and salmon broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"chicken and turkey meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken and turkey broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"chicken bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken bone broth": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"free-range chicken breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken breast 50%": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken breast 70%": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken breast 75%": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"chicken broth 24%": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"chicken broth 25%": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"chicken by- product meal": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken byproduct meal": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product meal": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product meal (a source of glucosamine and chondroitin sulfate)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product meal (natural source of clucosamine and chondroitin sulfate)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product meal (natural source of glucosamine)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product meal (source of chondroitin sulfate and glucosamine)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product meal (source of glucosamine & chondroitin sulfate)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product meal (source of glucosamine and chondroitin sulfate)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-product meal (source of glucosamine)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-products (organs only source of arginine)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken by-products (source of leucine and arginine)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"chicken cartilage": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilage (natural source of chondroitin sulfate & glucosamine)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilage (source of chondroitin & glucosamine)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilage (source of chondroitin sulfate and glucosamine)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilage (source of chondroitin sulfate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilage (a source of chondroitin sulphate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilage (source of glucosamine hydrochloride and chondroitin sulfate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilage (source of glucosamine)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilages ( source of glucosamine and chondroitin sulfate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken cartilages (source of glucosamine and chondroitin sulfate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken drumstick": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken eggs": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat preserved with natural mixed tocopherols (vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (mixed tocopherol preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (mixed tocopherol preserved)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (mixed tocopherols preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (mixed tocopherols used as a preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (naturally preserved with mixed tocopherols and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved naturally with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with  mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed natural tocopherols source of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed natural tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed natural tocopherols-a source of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed tocopherols & citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed tocopherols and ascorbic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed tocopherols and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed tocopherols and lactic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed tocopherols source of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with mixedtocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with natural mixed tocopherols (vitamin e))": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with natural mixed tocopherols and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with natural mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preserved with tocopherols and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat (preservedwith mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat preserved with ascorbic acid and citric acid": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat preserved with mixed tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat preserved with mixed tocopherols and citric acid": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken fat preserved with mixed tocopherols source of vitamin e": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"chicken giblets": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken gizzard": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken gizzards": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken hearts": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken liver digest": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken liver digest meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken liver dried": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken liver flavour": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"chicken liver flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"chicken liver hydrolysate": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken liver meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (a natural source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (a source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (natural source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (natural source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (preserved with mixed tocopherols)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (source of chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (source of glucosamine and chondroitin)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (source of glucosamine hydrochloride and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meal (source of methionine-cystine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"chicken meat": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken mince": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"chicken neck": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken necks": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"chicken organs": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken powder": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"chicken protein concentrate": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"chicken recipe - organic chicken with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken skin": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken soluble": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken tender": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken wheat gluten": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chicken with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"chickpea": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"chickpea flour": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"chickpeas": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"chickpeas flour": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"chicory": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"chicory extract": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"chicory root": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"chicory root (source of inulin)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"chicory root extract": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"chicory root inulin": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"chicoryroot": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"chitosan": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"chloine chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"chlorine chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cholecalciferol": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cholecalciferol (form of vitamin d3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cholecalciferol (source of vitamin d3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cholecalciferol (vitamin d3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"choline": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"choline bitartrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"choline chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"choline (choline chloride)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"choline chloride 50%": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"choline choline": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"choline choloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cholinechloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"chondroitin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"chondroitin sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"chondroitin sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"chopped asparagus": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"chorine chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cinnamon": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"citric acid": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid (a natural preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid (a preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid (a reservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid (for freshness)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid (preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid (preservatives)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid (used as a preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid for freshness": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citric acid preservative": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citricacid": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"citrus pulp": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"clams": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"clove": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"cloves": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"clucoasmine hydrochloride": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"cobalt amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobalt amino acid complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobalt carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobalt glucoheptonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobalt polysaccharide complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobalt proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobalt proteinate (source of chelated cobalt)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobalt sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobaltcarbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobaltglucoheptonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cobolt carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cocnut oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"coconut": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"coconut flavor": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"coconut flour": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"coconut meal": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"coconut milk": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"coconut oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"coconut oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"cod": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"cod (source of omega 3)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"cod liver": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"cod liver oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"cod meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"cod with ground bone": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"cold pressed sunflower oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"collard greens": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"color": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"color added titanium dioxide": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"colostrum": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"concentrated chicken protein": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"cooked chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"cooked wheat": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"cooper amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cooper amino acid complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cooper sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"coper amino acid complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper amino acid complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper amino acid complex (chelate)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper amino acidchelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper amino acids complex (chelate)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper gluconate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper glycine chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper glycine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper hydroxychloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper lysine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper lysine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper methionine hydroxy analogue chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper polysaccharide complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper proteinate (source of chelated copper)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper sulfate pentahydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copperamino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper-lysine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copperproteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper-proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"coppersulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"coral calcium": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn bran": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn flour": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn germ meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn gluten feed": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn gluten meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn grits": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn protein meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"corn protein concentrate": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn starch": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn starch modified": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn starchmodified": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn starch-modified": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"corn syrup": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"cottage cheese": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"couscous": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"crab": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"crab broth": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"crab meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"crab surimi": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"crab surimi (ocean whitefish crab broth)": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"crabmeat": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"cracked pearled barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"cherries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cranberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"mangos": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cranberry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cranberry extract": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cranberry fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"cranberry meal": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cranberry pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cranberry powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cremini mushrooms": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cricket": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"crushed red chili pepper": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"cucumber": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"cultured lactic acid bacteria": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"cultured lactic acid bacteria (e1707 enterococcus faecium dsm 10663-ncimb 10415)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"cultured whey": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"cumin": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"cupper sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cupric sulfate pentahydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cyanocobalamin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cyanocobalamin (source of vitamin b12)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cysteine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"cystine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d calcium pantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d- calcium pantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d -calcium pantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d/l methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-activated animal sterol (a source of vitamin d3 activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-activated animal sterol (source of vitamin d3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-alpha tocopherol": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-alpha tocopherol (source of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-alpha tocopherols": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-alpha tocopheryl acetate (form of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-alpha-tocopherol acetate (source of natural vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dandelion": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"dandelion greens": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"dandelion leaf": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"dandelion powder": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"dandelion root": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"d-biotin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium panotothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium panthothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium panto- thenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium pantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium pantothen-ate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium panto-thenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d\u2010calcium pantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium pantothenate source of vitamin b5": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium pantothenate (source of vitamin b5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium pantothenate (vitamin b5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium pantothenate (vitamin b-5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium pantothnenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calcium pnatothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-calciumpantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"de-boned alaskan pollock": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned alligator": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned arctic char": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned beef": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned bison": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"de-boned chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned cod": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"de-boned cod": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned duck": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"de-boned duck": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned goat": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned halibut": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned herring": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"de-boned herring": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned lamb": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"de-boned lamb": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned mutton": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned pork": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"de-boned pork": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned quail": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned rabbit": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"de-boned salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned tilapia": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned trout": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"de-boned trout": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"de-boned turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned venison": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"de-boned venison": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"deboned whitefish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned white\u00ffsh": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"deboned wild boar": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"de-boned wild boar": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"decaffeinated green tea extract": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"defatted wheat germ": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"defluorinated phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dehulled barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"dehulled soybean meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"dehydrated alfalfa": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dehydrated alfalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dehydrated alfalfameal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dehydrated apple": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated bifidobacterium thermophilum": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dehydrated bifidobacterium thermophilum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dehydrated blackcurrant berry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated blueberry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated boar": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated boar meat (source of glucosamine & chondroitin sulfate)": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated butternut squash": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated carrot": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated carrots": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated casein": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dehydrated chicken": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated chicken (source of glucosamine & chondroitin sulfate)": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"dehydrated cod": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"dehydrated egg": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated egg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"dehydrated eggs": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated enterococcus faecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dehydrated herring": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"dehydrated herring (source of glucosamine & chondroitin sulfate)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"dehydrated kelp": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"dehydrated lactobacillus acidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dehydrated lactobacillus casei fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dehydrated lamb": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated lamb meat (source of glucosamine & chondroitin sulfate)": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated mackerel": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"dehydrated pomegranate": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated pumpkin": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"dehydrated sardine": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"dehydrated seaweed meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"dehydrated spinach": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated sweet orange": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dehydrated turkey": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dehydrated whole chicken egg": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"dehydrated wild boar": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dextrose": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"dextrose anhydrous": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"digest": {
"Type": "Animal Digest",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often sourced from unnamed animals, making it an undesirable flavor enhancer with low nutritional value."
},
"d-galactose": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"source of dha": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dha": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dha (source of omega-3 fatty acids)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"eicosapentaenoic acid (epa) and docosahexaenoic acid (dha)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dha-docosahexaenoic acid and eicosapentaenoic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dha- docosahexaenoic acid and epa-eicosapentaenoic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"diatomaceous earth (an inert carrier and anti-caking agent)": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"dicalcium mononitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dicalcium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dicalsium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"diced chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"digestive enzymes amylase": {
"Type": "Animal Digest",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often sourced from unnamed animals, making it an undesirable flavor enhancer with low nutritional value."
},
"dill": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"di-methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dipotassium phospate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dipotassium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dipotassium sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"direct dehydrated alfalfa pellets": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"directdehydrated alfalfa pellets": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"disodium diphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"disodium edta": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"disodium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"disodium pyrophosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl -methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl- methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-alpha tocopherol (source of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-alpha tocopherol acetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-alpha tocopherol acetate (source of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dlalpha tocopheryl acetate (form of vitamin e)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-alpha-tocopherol acetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-alpha-tocopherolacetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dlmethionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl\u2013methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-methionine (an essential amino acid)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-methionine (essential amino acid)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dl-mthionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-mannose": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"docosahexaenoic acid (dha)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"docosahexaenoic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"docosahexaenoic acid (dha) (source of omega-3 fatty acids)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"docusate sodium": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"d-pantothenic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"dreid cranberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried  lactobacillus acidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried alfalfa": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dried alfalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dried algae (natural source of dha)": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"dried algae": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"dried apple": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried apple pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried apples": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried apricot": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"dried apricots": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"dried artichoke": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried aspergillus niger  fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillus niger fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillus niger fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillus niger fermentation product (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillus nigerfermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillus oryzae fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillus oryzae fermenation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillus oryzae fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillus oryzae fermentationproduct": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried aspergillusoryzae fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried avocado": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried b. animalis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillius subtillis fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus coagulans": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus coagulans fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus coagulans fermentation product.": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus coagulans fermentationproduct": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus coagulansfermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus coagulants fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus coagulans fermentation": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus licheniformis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus subtilis fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus subtilis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus subtilis fermentation product (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus subtilisfermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus subtillis fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus subtills fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus subtillus fermentaion extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bacillus subtilus fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried baciollus coagulans fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"bacillus coagulans fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried baciollus coagulans fermen-tation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried basillus subtilis fermentation products": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried beef stock": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried beet pulp": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried beet pulp (sugar removed)": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried beets": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried bifido bacterium bifidium thermophilum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bi\ufb01do bacterium bi\ufb01dium thermophilum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifido bacteriumbifidium thermophilum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium animalis fermaentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium animalis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bi\ufb01dobacterium animalis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium bifidium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifiobacterium bifidum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium bifidium thermophilum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium bifidum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium longum": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium longum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium thermophilum": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bifidobacterium thermophilum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried bilidobacterium longum": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried black soldier fly larvae": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"cooked bone marrow": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"dried blood": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried bluberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried blueberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried blueberry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried blueberry powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried brewer\u2019s yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried brewers yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried brewer's yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried broccoli": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried candida rugosa fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried candida rugose fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried carrot": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried carrots": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried celery": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried cellulose": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried citrus fruit pulp": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried chamomile": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"dried cheese": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried cheese powder": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried cheese product": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried chicken": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried chicken cartilage (source of chondroitin sulfate and glucosamine)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"dried chicken cartilage (source of glucosamine and chondroitin sulfate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"dried chicken flavored gravy": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"dried chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"dried chicken liver meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"dried chickory root": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried chickpeas": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dried chicory": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried chicory pulp": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried chicory root": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried chicory root (source of inulin)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried chicory root (source of soluble fiber)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried citrus pulp": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried clover extract": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dried coconut": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"dried colostrum": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried cranberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried cranberries salt": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried cranberry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried cranberry powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried cultured whey": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried dandelion": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"dried dandelion root extract": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"dried dried ginger": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried ediococcus acidilactici fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried egg": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried egg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"dried egg white": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried egg whites": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried egg yolks": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried eggs": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried entercoccus faecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococcus faecium": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococcus faecium fermentati on product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococcus faecium fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococcus faecium fermentation produce": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococcus faecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococcus faecium fermentationproduct": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococcus thermophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococcusfaecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried enterococus faecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried fermentation product dried l. casei fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried field peas": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dried fish broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"dried fish protein digest": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"dried garbanzo beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dried garlic": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried ginger": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried ginger root": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried goji berry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried golden algae": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"dried grape pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried green beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"dried green lipped mussel (source of lysine)": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"dried green lipped mussels": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"dried green-lipped mussels": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"dried ground blueberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried ground peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"dried ground potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried hydrolyzed casein": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried kale": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried kelp": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"dried kelp meal": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"dried l. acidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried l. reuteri fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilus fermentation": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilus": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilus fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophi-lus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilus fermentation product (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilus fermentation solubles": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilus fermentationproduct": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilus fermentration product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidophilusfermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidphilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus acidphophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus aciphophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus bulgaricus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus casei fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus casei fermentation solubles": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus casei fermentationproduct": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus casei fermentration product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus caseifermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus delbrueckii fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus fermentum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus lactis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus lactis fermentation solubles": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus plantarum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus plantarum fermentation product (lactosacc - probiotics)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus plantarumfermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus platarum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus reuteri ferme ntation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus reuteri fermentation": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillus reuteri fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillusacidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacilluscasei fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacillusplantarum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacilus acidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lactobacullus plantarum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried lavender": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"dried lentils": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"dried lettuce": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried liver digest": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"dried miscanthus grass": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried molasses": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"dried molasses beet pulp": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"dried mushroom": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried new zealand green mussels": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"dried new zealand green-lipped mussels": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"dried organic chicken broth": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"dried organic kelp": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"dried parsley": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"dried pea": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"dried peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"dried yellow peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"dried pediococcus acidilactici fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried pineapple": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried pineapple extract": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried plain beet fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried plain beet pulp": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried plain beet pulp (sugar removed)": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried plasma": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried pomegranate": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried porcine plasma": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried pork": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried pork broth": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried pork liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"dried pot marigold": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"dried potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried potato products": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried poultry protein": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"dried pumpkin": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried pumpkin flakes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried red cabbage": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried rhizopus oryzae fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried rhizopus oryzae fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried rhizopus oryzae fermentation product dried": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried rose hips": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried rosemary": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"natural preservative": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"dried saccharomyces cerevisiae fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried saccharomyces cerevisiae yeast culture": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried saccharomyces cerevisiae yeast extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried sccharomyces cerevisiae fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried seaweed meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"dried seaweed meal (ascophyllum nodosum)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"dried seaweed meal (ascophyllumnodosum)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"dried skim milk": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried skimmed milk": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried spearmint": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"dried spergillus niger": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried spinach": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried squash": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried streptococcus faecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried streptococcus faecium fermentationproduct": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried streptococcus thermophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried sweet orange": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried sweet potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried sweet potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried tapioca": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"dried tomato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried tomato paste": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried tomato pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried tomato powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried tomato puree": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried tomatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried trichoderma longbrachiatum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried trichoderma longibrachiatum": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried trichoderma longibrachiatum fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried trichoderma longibrachiatum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried trichoderma longibrachiatum fermentation extract. contains a source of live naturally occurring microorganisms": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried trichoderma longibrachiatum fermentation product (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried trichoderma reesei fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried trichodermalongibrachiatum fermentation extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried turmeric": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"dried watercress": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried whey": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried whey product": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried whey protein concentrate": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried white potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried whole cell algae (pure source of omega 3 dha)": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"dried whole egg": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"dried whole egg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"dried whole eggs": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"dried yam": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"dried yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried yeast culture": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dried yogurt": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"dried zucchini powder": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"driedbacillus coagulans fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"driedbacillus subtilis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"driedbifidobacterium bifidum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"driedchicory root": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"driedegg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"driedenterococcus faecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"driedlactobacillus acidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"driedlactobacillus casei fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"driedstreptococcus faecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"driedtomato pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"driedyeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"dry chicken broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"dry fish broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"dry pea flour": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"dry-aged ribeye flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"duck": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"duck (with ground bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck and turkey broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"duck bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"duck by-product meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"duck cartilage": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"duck fat (preserved naturally with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"duck fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"duck fat (preserved with natural mixed tocopherols and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"duck gizzard": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck bone broth": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"duck meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"duck necks": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck skin": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"duck wings": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"duck with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"d-xylose": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"egg": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"egg and chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"egg flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"egg noodle semolina": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"egg powder": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"whole egg powder": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"dried egg powder": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"egg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"egg product (dehydrated eggs)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"egg shell": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"egg shell meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"egg shell membrane collagen (source of glucosamine & chondroitin sulfate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"egg white": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"egg whites": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"egg yolk": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"eggplant": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"eggs": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"eggshell meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"eggshells": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"eicosapentaenoic acid (epa)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"elderberry juice": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"enriched pasta": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"enterococcus facecium": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"enterococcus faecieum": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"enterococcus faecium": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"enterococcus faecium fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"enterococcus faecium fermentation product (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"enterococcus faecium fermentation product dehydrated": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"enterococcus faecium product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"enzymes amylase": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"enzymes amylase (aspergillus oryzae)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"ergocalciferol (source of vitamin d2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"erythorbic acid (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"ethoxyquin (a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"ethylene diamine dihydriodide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ethylene diamine dihydroiodide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ethylenediamine dihydriodide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ethylenediamine dihydriodide (source of iodine)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ethylenediamine dihydroiodide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ethylenediamine dihydroiodide (source of iodine)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ethylenediaminedihydroiodide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"extruded soybeans": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"faba beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"fat product": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fava beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"fd&c blue #2": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"fd&c yellow #5": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"fd&c yellow #6": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"feed grade fat product (algae - source of fatty acids)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"feed grade fat product (algae source of fatty acids)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"feed grade fat product (source of fatty acids from algae)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"feed grade fat product algae": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"feeding oatmeal": {
"Type": "Grain Meals",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and of lower nutritional value than whole grains. Often used as fillers."
},
"fennel": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"fennel powder": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"fennel seed": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"fenugreek": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"fenugreek seed": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"fenugreek seeds": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"ferric pyrophosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferronyl iron": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous fumarate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous fumerate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous glycine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous glycine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous sulfate (source of iron)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous sulfate monohydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrous sulphate monohydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferroussulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ferrus sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"fiber vegetable of peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"field pea": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"field peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"filet mignon flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"fish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"fish bone broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"fish broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"fish protein concentrate": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"fish broth 19%": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"fish broth 23%": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"fish broth 24%": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"fish extract": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"fish extract (natural flavor)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"fish flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"crab flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"fish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"fish meal (100% salmon)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"fish meal (menhaden)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"fish meal (natural source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"fish meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"fish meal (source of omega 3 fatty acids)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"fish meal (source of ara-arachidonic acid)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"fish meal from 100% herring": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"herring fishmeal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"fish oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"\ufb01sh oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil ((source of dha) preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (menhaden)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (mixed tocopherol preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (natural source of dha)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (preserved with natural extracts rich in tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of ara arachidonic acid and dha-docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of ara- arachidonic acid and dha-docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of ara-arachidonic acid and dha- docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of ara-arachidonic acid and dha-docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha - docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha- docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha-docosahexaenoic acid and ara-arachidonic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha-docosahexaenoic acid and epa-eicosapentaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dhadocosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha-docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha-docosahexaenoicacid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of dha-docosahexanoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of eicosapentaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of epa-eicosapentaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil (source of omega 3 fatty acids)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil from 100% menhaden oil (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil from 100% menhaden oil mixed tocopherols (vitamin e) used as a preservative": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil menhaden (vitamin e mixed tocopherols used as a preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil source of ara-arachidonic acid": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil source of dha-docosahexaenoic acid": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil(preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"fish oil(source of omega 3 fatty acids)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"flaked ahi tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"flaked crab": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"flaked crab surimi": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"flaked tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"flavor enhancer": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"flax": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flax meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"flax seed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flax seed (source of omega 3)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flax seed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"flax seeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxmeal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"flaxseed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"\ufb02axseed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"organic flaxseeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (source of  omega 6 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (source of ome 3 and 6 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (source of omega 3 & 6 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (source of omega 3 & omega 6 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (source of omega 3 and 6 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (source of omega 3 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (source of omega 6 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (source of omega3 and 6 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed (sourceof omega 6 fatty acids)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed flakes": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"flaxseed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"flaxseed oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"flaxseed oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"flaxseeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"whole flax seed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"floric acid": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"flounder": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"\ufb02ounder": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"folate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid ": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid (vitamin b-5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid (vitamin b-7)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid (vitamin b9)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b9 (folic acid)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid (vitamin b-9)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid vitamin b-9": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid.": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid.  contains a source of live (viable)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folic acid. contains a source of live (viable)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"folicacid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"foloc acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"food starch": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"freeze-dried lamb meat": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried beef meat": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried beef": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried goat meat": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried beef": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried beef heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried beef kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried beef spleen": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried chicken": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried chicken (including ground chicken bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried chicken breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried chicken heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried chicken livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried cod": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"freeze dried cod liver": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"freeze-dried duck": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried duck (including freeze dried ground duck bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried egg": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried lamb": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried lamb heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried lamb kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried lamb liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried lamb spleen": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried pork fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"freeze dried pork heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried pork liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried pork livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freezedried pork": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried rabbit": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried rabbit (including freeze dried ground rabbit bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried rabbit kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried rabbit liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried rabbit lung": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"dried salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"freeze dried turkey": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze dried turkey heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried turkey liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze dried whitefish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"freeze-dried beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried beef tripe": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freezedried chicken": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried chicken": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried chicken pieces": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried cod liver": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"freeze-dried duck liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried goat liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried lamb": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried lamb liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried lamb tripe": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried pork liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried quail": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried raw beef": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried raw beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried raw chicken": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried raw chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried raw turkey": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried raw turkey liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"freeze-dried turkey": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"freeze-dried turkey liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried venison liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"freeze-dried whitefish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"fresh chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"fresh deboned chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"fresh duck": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"fresh herring": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"fresh whole sweet potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"fried bifidobacterium animalis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"fructo-oligosaccharides (fos)": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligiosaccharide (fos)": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligiosaccharides": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"frutooligosaccharide": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligocaccharide": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligosaccharide": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"frustooligosaccharide": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructo-oligosaccharide": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligosaccharide (fos)": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligosaccharide (prebiotic)": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligosaccharide (probiotics)": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligosaccharides": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligosaccharides (fos)": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligosacharide (fos)": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fructooligosccharides": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"fruit juice": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"fruit juice color": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"fucaceae": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"garbanzo bean": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"garbanzo beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"garlic": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"garlic oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"garlic oil a314421": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"garlic powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"garlic spice": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"gelatin": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"gelling agents": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"giblets": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"giner": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"ginger": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"ginger powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"ginger root": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"ginseng extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"gizzard": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"gla safflower oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"glucosamine": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"glucosamine hcl": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"glucosamine hydrochloride": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"glucosaminehydrochloride": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"glucose": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"glucose syrup solids": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"gluten meal": {
"Type": "Grain Meals",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and of lower nutritional value than whole grains. Often used as fillers."
},
"glycerin": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"glycerol monostearate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"glyceryl monostearate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"glycine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"goat": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"goat bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"goat cartilage": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"goat heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"goat kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"goat liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"goat lung": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"goat lungs": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"goat meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"goat milk": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"goat tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"golden algae": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"goose": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"grain distillers dried yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"grain sorghum": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"grape seed extract": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"gravy beef broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"gravy chicken broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"gravy turkey broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"green beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"green beef tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"green bell pepper": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"green bison tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"green lentils": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"green lipped mussel": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"green pea": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"green peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"green peppers": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"green tea": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"green tea extract": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"green venison tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"greenbeans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"grilled chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"grilled new york strip flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"grilled porterhouse steak flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"grilled steak flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"ground barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"ground beef": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"ground beef bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground beef bones": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground brewers rice": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"ground brown  rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"ground brown rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"ground chia seed": {
"Type": "Chia",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in omega-3s, fiber, and antioxidants, chia seeds are a good addition in moderation for coat health and digestion."
},
"ground chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"ground chicken bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground cinnamon": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"ground cod with bones": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"ground corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"ground cumin": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"ground dried chickpeas": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"ground dried peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"ground duck with bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground egg shells": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"ground fennel": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"ground flax seed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"ground flaxseed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"ground flaxseed (source of omega 3)": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"ground flaxseed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"ground flaxseeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"ground ginger": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"ground grain sorghum": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"ground lamb bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground lamb bones": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground lentils": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"ground limestone": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ground millet": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"ground miscanthus grass": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"ground oats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"ground pearled barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"ground peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"ground green peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"ground pecan shells": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"ground pecan nut shells": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"ground peppermint": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"ground pork": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"ground pork bones": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground pumpkin seed": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"ground pumpkin seeds": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"ground rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"ground rosemary": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"ground salmon with bones": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"ground sorghum": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"ground soybean hulls": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"ground tapioca": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"ground thyme": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"ground turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"ground turkey bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground turkey with bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground venison bones": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"ground wheat": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"ground white rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"ground whole barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"ground whole brown rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"ground whole corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"ground whole flaxseed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"ground whole flaxseed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"ground whole grain barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"ground whole grain corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"ground whole grain sorghum": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"ground whole grain wheat": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"ground whole wheat": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"ground whole white rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"ground yellow corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"ground yellow mustard": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"grouper": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"guar gum": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"guargum": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"guinea fowl": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"guinea fowl meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"guineafowl": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"gum": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"gum ghatti": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"haddock": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"hake": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"halibut": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"ham": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"ham & egg flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"hare meat": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"hcl": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"heart gizzard": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"hemicellulase (trichoderma reesei)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"hemicellulose extract": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"herring": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"herring & salmon oil blend (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"herring (source of glucosamine & chondroitin sulfate)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"herring broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"herring meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"herring meal (source of chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"herring meal (source of glucosamine )": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"herring meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"herring meal (source of omega 3)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"herring meal from ocean caught herring": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"herring oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"herring oil (preserved with mixed tocopherols source of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"herring oil (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"herring oil (source of dha)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"herring oil (source of dha-docosahexaenoic acid & epa-ecosapentaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"herring oil (source of omega 3 fatty acids)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"high fructose corn syrup": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"highly branched inulin": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"histidine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"hoki": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"hoki oil": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"honey": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"human grade wild-caught sockeye salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"hydrochloric acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"hydrolized chicken": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"hydrolyzed chicken": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"hydrolyzed chicken flavor": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"hydrolyzed chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"hydrolyzed corn gluten": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"hydrolyzed corn protein": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"hydrolyzed fish protein": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"hydrolyzed pork": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"hydrolyzed potato protein": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"hydrolyzed poultry by-products aggregate": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"hydrolyzed salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"hydrolyzed salmon protein": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"hydrolyzed soy protein": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"hydrolyzed soy protein isolate": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"hydrolyzed wheat gluten": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"hydrolyzed yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"hydrolyzed yeast (actigen - probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"hydrolyzed yeast (actigen\u2122 prebiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"hydrolyzed yeast (source of beta glucans)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"hydrolyzed yeast (source of betaglucans)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"icelandic fish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"imitation crab water": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"inactive selenium yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"inositol": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"inulin": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"inulin (a source of dietary fiber)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"inulin (chicory root)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"inulin (from chicory root)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"inulin (jerusalem artichoke)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"inulin (prebiotic)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"iodine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iodine amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iodine aminoacid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iodine cobalt carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iodized salt": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iodizedsalt": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron amino acid complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron amino acid complex (chelate)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron amino acidchelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron amino chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron glycinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron glycine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron monohydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron oxide (color)": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"iron oxide color": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron oxide colorant": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron polysaccharide complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron polysaccha-ride complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"copper polysaccha-ride complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron protein": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iodine proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron proteinate (source of chelated iron)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"iron sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ironamino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"jerusalem artichoke": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"juniper berries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"k9 mobility powder": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"kale": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"kale powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"kale puree": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"kangaroo": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"kangaroo broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"kangaroo meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"kelp": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"kelp meal": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"kelp meal (ascophyllum nodosum)": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"kelp powder": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"krill meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"krill meal (source of dha-docohexaenoic acid & epa- eicosapentaenoic acid)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"l- ascorbyl-2-polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphat": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l ascrobyl polyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l- carnitine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l carnitine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l lysine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-abscorbyl-2-polyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"lactase": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactase (aspergillus oryzae)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactic acid": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"lactic acid (used as a preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"lactobaccillus casei": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobaccillus casei fermentation product dehydrated": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus acidophilus": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus acidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus acidophilus fermentation product (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus acidophilus fermentation product dehydrated": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus aciphophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus casei": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus casei fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus casei fermentation product (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus casei fermentation product dehydrated": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus casei fermentation solubles": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus casei fermentration products": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus fermentum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus lactis": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus plantarum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lactobacillus reuteri fermentation product dehydrated": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"l-alanine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"lamb": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"lamb (source of glucosamine)": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"lamb (with ground bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb and chicken broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"lamb blood": {
"Type": "Blood & Plasma",
"Quality": "Poor Quality",
"Quality Description": "Low-quality, heavily processed by-products used to increase protein content cheaply. Unnecessary in high-quality diets."
},
"lamb bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb bone broth": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"lamb cartilage": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"lamb fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"lamb heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb hearts": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb lung": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"lamb meal (natural source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"lamb meal (source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"lamb meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"lamb meat": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"lamb meat cubes": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"lamb plasma": {
"Type": "Blood & Plasma",
"Quality": "Poor Quality",
"Quality Description": "Low-quality, heavily processed by-products used to increase protein content cheaply. Unnecessary in high-quality diets."
},
"lamb spleen": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb tail": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb tongue": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lamb tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"lambtripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"l-arginine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-as corbyl-2-polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-asccorbyl-2-polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl 2- polyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl- 2-polyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl 2-polyphosphate (source of vitamin c activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl -2-polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl- 2-polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2- polyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2 polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2- polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2- polyphosphate (vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-poly- phosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphophate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphoshate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphoshphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate (a source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate (source of ascorbic acid)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphos-phate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascor-byl-2-polyphosphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate (source of vitamin c)(": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate (source ofvitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate (sourceof vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate (vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate source of vitamin c": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphosphate(source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascorbyl-2-polyphsphate (source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascrobyl-2-polyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-ascrobyl-2-polyphosphate (a source of vitamin c)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-aspartic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"lavender": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"lcarnitine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-carnitine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-cysteine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-cysteine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-cystine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"lecithin": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"lecithin (sunflower derived)": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"lemon balm": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"lemon juice": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"lentil fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"lentil \ufb01ber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"lentil flour": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"lentil starch": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"lentils": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"lettuce": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"leucine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-glutamic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-histidine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"licorice": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"lima beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"linden flowers": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"linseed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"linseeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"lipase": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lipase (aspergillus oryzae)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"lipoic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"liquid bifidobacterium animalis fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"liquid egg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"liquid lactobacillus acidophilus fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"liquid lactobacillus casei fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"liquid lactobacillus reuteri fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"l-isoleucine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"liver flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"l-leucine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-lysine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-lysine (an essential amino acid)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-lysine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-lysine monohydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"lobster": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"lobster broth": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"lobster consomm\u00e9": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"lobster meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"locust bean": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"locust bean gum": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"long chain inulin": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"long grain rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"l-phenylalanine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-proline": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-serine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-threonine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-tryptophan": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"l-tyrosine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"lumpfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"l-valine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"lycopene": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"lysine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"mackerel": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"mackerel (source of omega 3)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"mackerel 45%": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"mackerel cutlets": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"mackerel flakes": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"mackerel meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"madnesium oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"maganese proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"maganese sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"managanese sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnase amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnese proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnessium proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium sulfate monohydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesium sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"magnesiumoxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"malt extract": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"malted barley": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"malted barley extract": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"malted barley flour": {
"Type": "Brewers Products",
"Quality": "Poor Quality",
"Quality Description": "Low-quality by-products of the brewing process. Often used as cheap fillers with limited nutritional value."
},
"maltodextrins": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"managese proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"mananous oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese amino acid complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese amino acid complex (chelate)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese amino acids chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese copper proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese gluconate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese glycine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese hydroxychloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese methionine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese methionine hydroxy analogue chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese methioninecomplex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese polysaccharide complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese polysaccharide complex and copper polysaccharide complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese protein": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese protein ate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese proteinate (source of chelated manganese)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese sulfate monohydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganese sulphate monohydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganesemethionine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganeseproteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganesesulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganous oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganous proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"manganous sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"mango": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"mannese amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"marigold": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"marigold extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"marigold extract (tagetes erecta l.)": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"marigold petal": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"marine microalgae": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"marine microalgae (source of dha & epa)": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"marine microalgae (source of dha)": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"marine microalgae oil": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"marine microalgae oil (preserved with mixed tocopherols)": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"meat & bone meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"meat and bone meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"meat and bone meal (source of calcium)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"meat broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"meat by products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"meat by-product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"meat by-products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"dried meat by-products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"meat meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"meat protein isolate": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"medium-chain triglyceride vegetable oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"melon": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"menadion sodium bisulfate complex (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadion sodium bisulfite complex (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione bisulfite complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione bisulfite complex (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione bisulfite complex (vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione nicotinamide bisulfite (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfate (source of vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfate complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfate complex (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfate complex (source of vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfate complex (vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite (source of vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite (vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex vitamin k": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisul\ufb01te complex (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisul\ufb01te complex (source of vitamin k activity))": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (source of vitamin k activity))": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (source of vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (source of vitamin k))": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (source of vitamin k3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (source of vitamin k3))": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bifulfite complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex (vitamin k3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex source of vitamin k activity": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulfite complex(source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulphite complex (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium bisulphite complex (source of vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodiumbisulfite complex (source of vitamin k activity)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadoine sodium bisulfite complex (vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menhaden fish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (a source of fish oil)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (a source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (mixed tocopherol preservative)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (preserved with mixed tocopherols)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (source of chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (source of dha-docosahexaenoic acid)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (source of dha)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (source of omega 3 fatty acid)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (source of omega 3 fatty acids)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (source of omega-3 fatty acids)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish meal (source of taurine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden fish oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fish oil (mixed tocopherols used as a preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fish oil (preserved with mixed natural tocopherols source of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fish oil (preserved with mixed natural tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fish oil (preserved with mixed natural tocopherols-a source of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fish oil (preserved with mixed tocopherol)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fish oil (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fish oil (source of dha)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fish oil a source of epa": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhaden fishmeal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden herring meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"menhaden oil (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"menhadon meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"methionine supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"microbial enzyme": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"miinerals zinc amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"milk": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"milk solids": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"millet": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"millet pearl grain": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"milo": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"milo natural flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"mineral oil": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"mineralpotassium chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"minerals ferrous sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"minerals manganese sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"minerals zinc amino acid complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"min\u00e9rals zinc oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"minerals zinc proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"mineralszinc sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"minnows": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"mint": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"miscanthus grass": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"miscanthus grass fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"mixed tocopherals (a source of vitamin e)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherol (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols & citric acid (preservatives)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (a natural preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (a natural source of vitamin e)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (a source of vitamin e)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (added to preserve freshness)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (as preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (for freshness)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (for added freshness)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (natural preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (preservative and a form of vitamin e)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (preservative-form of vitamin e)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (to preserve freshness)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols (used as a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols added to preserve freshness": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols and bha (preservatives)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols and citric acid (preservatives)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols and rosemary extract": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols for added freshness": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols for freshness": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols preserved": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mixed tocopherols with rosemary (preservatives)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"mized tocopherols & citric acid (preservatives)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"modified corn starch": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"modified food starch": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"modified rice starch": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"tapioca starch-modified": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"modified tapioca starch": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"molasses": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"monk\ufb01sh": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"monkfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"mono and dicalcium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"mono and diglycerides": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"monocalcium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"monocalcium phsophate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"monodicalcium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"monoglycerides": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"monopotassic phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"monosodium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"montmorillonite": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"montmorillonite clay": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"mung bean": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"muskmelon": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"mussel": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"mussels": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"mustard greens": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"mustard seed powder": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"mutton": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"mutton bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"mutton liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"mutton lung": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"mutton meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"mutton tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"natual flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural & artificial flavors": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"natural and artificial flavor (source of grilled flavor)": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"natural and artificial flavors": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"natural and artificial roasted turkey flavor": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"natural antioxidant": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"natural bacon flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural beef flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural beef flavor (source of steak flavor)": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural vinegar": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"natural buffered vinegar": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"buffered vinegar": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"natural butter flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural chicken and turkey flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural chicken \ufb02avor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural chicken liver flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural cod \ufb02avor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural color": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"natural duck flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural filet mignon flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural fish flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural fish flavour": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural \ufb02avor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural flavor (source of grilled chicken flavor)": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural flavor (source of prime rib flavor)": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural flavoring": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural flavors": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural flavour": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural grill flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural grilled chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural grilled steak flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural hickory smoke chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural hickory smoke flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural hickory smoked chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural lamb flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural lamb flavour": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural liver flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural liver flavors": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural microorganisms": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"natural mixed tocopherols": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"natural new york strip flavor": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"natural omega blend": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"natural parmesan and butter flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural pork flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural pork tenderloin flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural porterhouse flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural porterhouse steak flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural poultry flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural prime rib flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural rabbit flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural roasted beef flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural roasted chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural roasted flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural roasted turkey flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural rotisserie chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural salmon flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural sauteed seafood flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural seared salmon flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural smoke flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural smoked bacon flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural steak flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural t-bone steak flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural tocopherols": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"natural top sirloin flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural tuna flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural turkey and chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural turkey flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural vegetable flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural vegetable flavoring": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural vegetable flavors": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural vegetarian flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural well water": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"natural white meat chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural whitefish flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"natural yeast flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"naturalflavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"naturally occurring microorganisms": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"naturally preserved with mixed-tocopherols": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"naturel flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"navy beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"n-butyric acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"new york strip flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"new zealand grass-fed lamb green tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"new zealand green lipped mussels": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"new zealand green mussel": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"new zealand green mussel (source of glucosamine & chondroitin sulfate)": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"new zealand green mussels": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"new zealand lamb tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"new zealand mussel": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"new zealand sea mussel": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"niacin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin (source of vitamin b3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin (vitamin 133)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin vitamin b-3": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin (vitamin b3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin (vitamin b-3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin supplement vitamin b3": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin vitamin b3": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin supplement (source of vitamin b3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin supplement (vitamin b3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin supplement (vitaminb3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b3 (niacin supplement)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacin supplemment": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacinamide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"niacinsupplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"nicacin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"nicin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"nicotinic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"nicotinic acid (source of vitamin b3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"nicotinic acid (vitamin b3 supplement)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"nicotinic acid (vitamin b3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"nicotinic add (source of vitamin b3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"norkotah potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"nutritional yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"oat bran": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"oat fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"oat flour": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"oat groats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"oat hulls": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"oat hulls (source of fiber)": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"oat meal": {
"Type": "Grain Meals",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and of lower nutritional value than whole grains. Often used as fillers."
},
"oatmeal": {
"Type": "Grain Meals",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and of lower nutritional value than whole grains. Often used as fillers."
},
"oats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"ocean fish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"ocean fish (sardine and mackerel)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"ocean fish (source of omega 3)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"ocean fish broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"ocean fish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"ocean herring meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"ocean white fish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"ocean whitefish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"ocean whitefish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"oceanfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"oceanfish broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"oceanfish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"oil of rosemary": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"okra": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"oligofructose": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"olive oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"olive oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"olive oil preserved with mixed tocopherols": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"omega 3": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"omega 3 & 6 from fish oil": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"orange": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"orange juice": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"oranges": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"oregano": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"organic alfalfa": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic alfalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic amaranth": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic amarath": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic apple": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic apple cider vinegar": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic apples": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic banana": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic bananas": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"organic barley grass": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"organic barley grass powder": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"organic beef": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"organic beef kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic beets": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic blueberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic blueberry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic broccoli": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic brown rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"organic butternut squash": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic canola meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"organic carrot": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic carrots": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic cassava root flour": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"organic celery": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"organic chicken broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"organic chicken fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"organic chicken fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"organic chicken gizzard": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic chicken heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic chicken liver digest meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"organic chicken livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic chicken meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"organic chicken with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic chickpea": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic chickpeas": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic chicory root (source of inulin)": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"organic cilantro": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic coconut flour": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"organic coconut oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"organic cranberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic cranberry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic deboned chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"organic dehydrated alfalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic dehydrated chicken": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"organic dehydrated kelp": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"organic dried alfalfa": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic dried alfalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic dried egg": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"organic dried egg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"organic dried eggs": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"organic dried kelp": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"organic dried kelp meal": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"organic dried liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic dried pea": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"organic dried peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"organic dried potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic dried seaweed meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"organic dried spinach": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic egg": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"organic egg shell": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic flaxseed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"organic flaxseed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"organic garlic powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic ginger": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic ground alfalfa": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic guar gum": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"organic kale": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic kelp": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"organic lentils": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic liver digest meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"organic locust bean gum": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic long chain inulin": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"organic lupin": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"organic mangoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic natural flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"organic oatmeal": {
"Type": "Grain Meals",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and of lower nutritional value than whole grains. Often used as fillers."
},
"organic oats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"organic olive oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"organic parsley": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"organic pea flour": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"organic pea hulls": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"organic pea protein": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"organic pea starch": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"organic peanut butter": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"peanut butter": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"organic peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"organic potato flour": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic potato starch": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic potatoes flour": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic pumpkin": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic pumpkin seed": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic pumpkin seeds": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic quinoa": {
"Type": "Quinoa",
"Quality": "Acceptable Quality",
"Quality Description": "A good source of protein and amino acids but should not be a primary ingredient. Can be used as an alternative to grains for some dogs."
},
"organic rosemary": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"organic rosemary extract": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"organic sage": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"organic soybean oil (preserved with natural mixed tocopherols and citric acid)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"organic spinach": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic squash": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic strawberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic sunflower oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"organic sunflower oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"organic sunflower seed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"organic sunflower seed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"organic sunflower seeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"organic sweet potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic sweet potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic tapioca": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"organic tapioca starch": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"organic tapoica": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"organic turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"organic turkey and chicken broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"organic turkey heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic turkey liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic turkey with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"organic turmeric": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"vegetable oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"organic vegetable oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"organic wheat grass": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"organic whole egg": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"organic wild blueberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"organic yeast extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"oven roasted chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"pacific cod": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"pacific ocean fish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"pacific rockfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"pacific sole": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"pacific tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"pacific whiting": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"pacific whiting meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"pacific whiting meal (natural source of glucosamine and chondroitin)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"palm oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"pantothenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pantothenic acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pantothenic acid (vitamin b5)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pantothenic acid pyridoxine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"papain": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"papaya": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"papaya extract": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"papaya powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"papayas": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"papaye": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"paprika": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"paprika (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"paprika extract (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"paprika powder": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"parsely": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"parsley": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"parsley flake": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"parsley flakes": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"parsnip": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"parsnips": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"partially hydrogenated canola oil preserved with tbhq": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"pasta": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"pasta wheat flour": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"pbridoxine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pcmx": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"pea": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea bran meal": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea fiber": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea \ufb01ber": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea fibre": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea flour": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea hull fiber": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea powder": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea protein": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea protein concentrate": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea protein isolate": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea pulse protein": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pea starch": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"peanut hearts": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"peanuts": {
"Type": "Nuts",
"Quality": "Poor Quality",
"Quality Description": "Potential allergen and difficult for dogs to digest; can be high in fat, leading to digestive issues and weight gain."
},
"pearled barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"pearledbarley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"pears": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"peas-ground": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"pectin": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pepper": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"peppermint": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"peppermint leaf powder": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"pheasant": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"phosphoric acid": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pineapple": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pineapple stem": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pineapple stem (source of bromelain)": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pinto beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"plaice": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"plain dried beet pulp": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"plums": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pollock": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"pollock broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"pollock meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"pollock oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"polyhauai'i berry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pomegranate": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pomegran-ate": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pomegranate extract": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pomegranate powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pomegranates": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pommace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"porcine animal fat preserved with bha": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"porcine animal fat preserved with bha and citric acid": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"porcine meat and bone meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"porcine meat meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"porcine plasma": {
"Type": "Blood & Plasma",
"Quality": "Poor Quality",
"Quality Description": "Low-quality, heavily processed by-products used to increase protein content cheaply. Unnecessary in high-quality diets."
},
"pork": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"pork (with ground bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork and bone meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"pork bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork bone broth": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"pork by-products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"pork cartilage": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork digest": {
"Type": "Animal Digest",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often sourced from unnamed animals, making it an undesirable flavor enhancer with low nutritional value."
},
"pork digest (source of collagen)": {
"Type": "Animal Digest",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often sourced from unnamed animals, making it an undesirable flavor enhancer with low nutritional value."
},
"pork fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"pork fat (mixed tocopherol preserved)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"pork fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"pork fat (preserved with mxed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"pork fat (preserved with tbhq and citric acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"pork flavor": {
"Type": "Artificial Flavors",
"Quality": "Poor Quality",
"Quality Description": "Offer no nutritional benefit and may contribute to allergic reactions or food sensitivities in dogs."
},
"pork gelatin": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"pork heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork hearts": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork liver broth": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork liver flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"pork livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork lung": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork lungs": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"pork meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"pork meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"pork meat meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"pork meat solubles dehydrated": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"pork plasma": {
"Type": "Blood & Plasma",
"Quality": "Poor Quality",
"Quality Description": "Low-quality, heavily processed by-products used to increase protein content cheaply. Unnecessary in high-quality diets."
},
"pork protein concentrate": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"pork protein isolate": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"pork spleen": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"porterhouse steak flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"postassium chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pot assium alginate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium alginate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium choride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium citrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium cl": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium iodate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium iodide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium iodide (source of iodine)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium iodine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium lodide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium sorbate (a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"potassium sorbate (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"potassium sorbate (used as a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"potassium sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassium sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassiumchloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potassuim chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"potato fiber": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"potato flour": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"potato protein": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"potato starch": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"olives": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"poultry": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"poultry by-product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"poultry and pork digest": {
"Type": "Animal Digest",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often sourced from unnamed animals, making it an undesirable flavor enhancer with low nutritional value."
},
"poultry broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"poultry by-product mea": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"poultry by-product meal": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"poultry by-product meal (a source of glucosamine and chondroitin sulfate)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"poultry by-product meal (natural source of glucosamine)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"poultry by-product meal (source of glucosamine)": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"poultry by-products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"poultry digest": {
"Type": "Animal Digest",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often sourced from unnamed animals, making it an undesirable flavor enhancer with low nutritional value."
},
"poultry fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"poultry fat from 100% chicken mixed tocopherols (vitamin e) used as a preservative": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"poultry fat from chicken (vitamin e mixed tocopherols used as a preservative)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"poultry fat preserved with bha": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"poultry giblets": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"poultry heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"poultry hearts": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"poultry liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"poultry livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"poultry meal (100% chicken duck and turkey)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"poultry meal from 100% chicken": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"powdered cellulose": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"powdered psyllium seed husk": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"prawn": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"prawn 23%": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"prawns": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"prebiotic/probiotic blend": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"preserved with citric acid": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"(preserved with mixed tocopherols)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"preserved with mixed tocopherols": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"preserved with mixed tocopherols (form of vitamin e)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"preserved with mixed tocopherols and citric acid": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"preserved with mixed-tocopherols": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"preserved with natural mixed tocopherols": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"preservedwith mixed tocopherols": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"pressed cranberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"primary dried yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"prime rib flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"propionate zinc proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"propyl gallate": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"propylene glycol": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"protease": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"protease (aspergillus oryzae)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"psyilium seed husks": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"psyllium": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"psyllium husk": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"psyllium husks": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"psyllium seed husk": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"psyllium seed husks": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"pumpkin": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkin 24%": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkin flakes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkin meal": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkin powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkin puree": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkin seed": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkin seeds": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkins": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkinseed": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pumpkinseeds": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"purified water": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"purple potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"pyrdoxine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridixoine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxidine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridox": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine (vitamin b6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydro- chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydroc hloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxin hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochoride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride vitamin b-6": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyroxidine hydrochloride (vitamin b-6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochlo-ride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydro-chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b6 (pyridoxine hydrochloride)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride (b6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride (source of vitamin b6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride (source of vitaminb6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride vitamin b6": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride (vitamin b6 supplement)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride (vitamin b6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride (vitamin b-6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride (vitaminb6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrochloride source of vitamin b6": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrocholoride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrocholoride (souce of vitamin b6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hydrocloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxine hyrdochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyridoxinehydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyriodoxine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyroxidine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"pyroxidine hydrochloride (source of vitamin b6)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"quail": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"quail broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"quail egg": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"quineafowl": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"quinoa": {
"Type": "Quinoa",
"Quality": "Acceptable Quality",
"Quality Description": "A good source of protein and amino acids but should not be a primary ingredient. Can be used as an alternative to grains for some dogs."
},
"quinoa seed": {
"Type": "Quinoa",
"Quality": "Acceptable Quality",
"Quality Description": "A good source of protein and amino acids but should not be a primary ingredient. Can be used as an alternative to grains for some dogs."
},
"rabbit": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"rabbit (including ground rabbit bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit (with ground bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"rabbit heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit hearts": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit kidneys": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit lung": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit lungs": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"rabbit meat": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"rabbit recipe - rabbit with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rabbit with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"rainbow trout": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"raspberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"read-sedge peat": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"real chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"red #3": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"red #40": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"red 3": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"red 40": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"red 40 lake": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"red algae": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"red bell pepper": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"red bigeye": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"red delicious apples": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"red iron oxide": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"red lentils": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"red meat": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"red pepper extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"red peppers": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"red rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"reduced iron": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"reed-sedge peat": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"ribflavin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ribo avin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ribo\u02dbavin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ribo\u02ddavin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboavin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ribo\ufb02avin": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin (b2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin (source of vitamin b2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement vitamin b-2": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin (vitamin b2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ribo\ufb02avin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement vitamin b2": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement (source of vitamin b2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ribo\ufb02avin supplement (vitamin b2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"ribo\ufb02avin supplement (source of vitamin b2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b2 (riboflavin supplement)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement (vitamin b2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement (vitamin b-2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement (vitamin v-2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement (vitaminb2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement source of vitamin b2": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavin supplement(vitamin b2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavinsupplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"riboflavinsupplement(sourceofvitaminb2)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice 1%": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice 6%": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice 3%": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice bran": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice bran (solvent extracted)": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice bran (stabilized)": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice bran oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"rice flour": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice hulls": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice noodle": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice pasta": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice protein concentrate": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"rice starch": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"roasted bison": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"roasted duck": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"roasted lamb": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"roasted peanut oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"roasted quail": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"roasted venison": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"roboflavin supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"rock salt": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"rolled oats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"romaine lettuce": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"rose hips": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"rosehips": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"rosemary": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"rosemary extract": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"rosemary extract.": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"rosemary powder": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"rotisserie chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"ructooligosaccharide": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"russet burbank potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"russet potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"rye": {
"Type": "Rye",
"Quality": "Poor Quality",
"Quality Description": "Can be hard for dogs to digest and is less nutritionally valuable compared to other grains like oats or rice. May cause digestive upset."
},
"rye flour": {
"Type": "Rye",
"Quality": "Poor Quality",
"Quality Description": "Can be hard for dogs to digest and is less nutritionally valuable compared to other grains like oats or rice. May cause digestive upset."
},
"saba": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"saccharomyces cerevesiae fermentation soluble": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"saccharomyces cerevesiae fermentation solubles": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"saccharomyces cerevisae yeast cluture": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"saccharomyces cerevisiae fermentation solubles": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"saccharomyces cerevisiae yeast culture": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"safflower oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"safflower oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sage": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"sage extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"salmon (source of dha)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"salmon (source of glucosamine)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"salmon (source of omega 3)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"salmon (source of omega-3)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"salmon broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"salmon hydrolysate": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"salmon meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (natural source of glucosamine and chondroitin)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (source of chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (source of chondroitinsulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (source of dha)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (source of omega 3)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (source of omega-3 fatty acids)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (source of omega-3)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon meal (source of omega 3 fatty acids)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"salmon oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (a source of dha)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (preserved with miced tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (preserved with mixed tocopherols source of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (preserved with mixed tocopherols) (source of dha)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (preserved with natural mixed tocopherols a source of vitamin e)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (preservedwith mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (presevered with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (source of dha & epa)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (source of dha)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (source of dha-docosahexaenoic acid and epa-eicosapentaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (source of dha-docosahexaenoic acid)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (source of omega 3 fatty acids)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil (source of omega 3)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil preserved with mixed tocopherols": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil(preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon oil(preserved with tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"salmon skin": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"salmon with ground bone": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"salt": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sardine": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole sardine": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sardine (source of omega 3)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sardine broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"sardine consomm\u00e9": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sardine cutlets": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sardine meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"sardines": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sardines (source of fish)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sardines cutlets": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sarsaparilla": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"sarsaparilla root": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"scallop flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"scallops": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"schidigera extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"scrambled egg and sausage flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"sea bass": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"sea bream": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sea cucumber": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"sea salt": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"seabass": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"seabass broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"seabream": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"seaweed": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"seaweed 5%": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"seaweed-derived calcium": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"seium selenite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"selenium": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"selenium beast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"selenium premix": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"selenium proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"selenium selenite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"selenium yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"selenium yeast (inactive)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"selenium yeast (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"selenium yeast (selplex)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"sesame oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sesame oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sesame seed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"sesame seeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"sesame seeeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"shiitake": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"shirasu": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"shrimp": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"shrimp meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"shrimp meal (source of chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"shrimp meal (source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"shrimp meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"silicon dioxide": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"silver carp": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"silver hake": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"skimmed milk": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"skipjack": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"skipjack tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"smoked bacon": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"smoked salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"smoked tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"smoked turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"smoke-flavored salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"smoke-flavored turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"snapper": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"snow peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"sockeye salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sodium": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium acid pryophosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium acid pyrophosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium acid pyrophosphate (source of phosphorus)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium alginate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium aluminosilicate": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"sodium ascorbate": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium ascorbate (a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium benzoate (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium bicarbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium bisulfate": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"sodium carbonate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium carboxymethylcellulofse": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"sodium carboxymethylcellulose": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"methyl cellulose": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"sodium caseinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium chloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium delenite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"chelated sodium selenite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium edta": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"sodium erythorbate": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium erythrobate (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium erytrobate (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium hexametaphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium nitrite": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium nitrite (for color retention)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium nitrite (to promote color retention)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium nitrite (to promote color retention) (to promote color retention)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium phosphate monobasic": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium propionate (a preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"sodium pyrophosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium selemite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium selenate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium selenite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium selenite.": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium selenite. inactive ingredients: disodium edta": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium selenium": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium silico aluminate": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"sodium triopolyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium triphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium triployphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium tripolyphosp hate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium tripolyphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium tripolyphsphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodium yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"sodiumacid pyrophosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodiumphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sodiumselenite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"soidum selenite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"soldium selenite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sole": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"sorbic acid (a preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"sorbic acid (preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"sorbic acid (used as a preservative)": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"sorghum": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"soya meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soy flakes": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soy flour": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soy grits": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soy hulls": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soy lecithin": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soy oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"soy protein concentrate": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soy protein isolate": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soybean germ meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soybean hulls": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soybean meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soybean mill run": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soybean mill": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"soybean oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"soya bean oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"soybean oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"spearment": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"spearmint": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"spearmint extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"spearmint extract.": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"spearmint extract. this is a naturally preserved product": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"spelt": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"spinach": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"spinach greens": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"spinach powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"spirulina": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"split peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"spray dried animal blood cells": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"spray dried beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"spray dried beef plasma": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"spray dried chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"spray dried egg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"spray dried porcine plasma": {
"Type": "Dried Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Retains nutritional value and provides a high-protein source, but quality depends on the drying process and meat source."
},
"spray dried pork liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"squash": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"squid": {
"Type": "Seafoods",
"Quality": "Acceptable Quality",
"Quality Description": "Nutritionally valuable when from safe, clean sources, rich in protein and healthy fats, but sourcing transparency is important."
},
"starch": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"steamed bone meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"steelhead trout": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"strawberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"strawberry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"sucrose": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"sufficient water for processing": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"water sufficient for processing 26%": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"protein hydrolysate": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"sugar": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"sulfur": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"sun cured ground miscanthus grass": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"sun ower oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sun\u02dbower oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"suncured alfalfa": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"sun-cured alfalfa": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"suncured alfalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"sun-cured alfalfa meal": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"sunflower chips": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"sunflower lecithin": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"sunflower meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"sunflower oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sun\ufb02ower oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sunflower oil (mixed tocopherol preserved)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sunflower oil (preserved with citric acid)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sunflower oil (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sunflower oil (source of omega 6 fatty acids)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sunflower oil preserved with mixed tocopherols": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sunflower seed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"sunflower seed oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"sunflower seeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"sun\ufb02ower seeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"sweet basil": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"sweet potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"sweet potato puree": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"sweet potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"sweetpotatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tannic acid": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"tapioca": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"tapioca flour": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"tapioca root": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"tapioca starch": {
"Type": "Roughages",
"Quality": "Acceptable Quality",
"Quality Description": "Provides dietary fiber to support digestion, but should be from recognizable sources like fruits, vegetables, or whole grains."
},
"tart cherry": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"taurine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"taurine (an essential amino acid)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"taurine and vitamin supplements": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"t-bone steak flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"tea": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"tea extract": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"tetra sodium pyrophosphate": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"tetrasodium pyrophosphate": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"tfd nutrient blend": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"th iamine mononitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thaimine mononitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamin mononitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamin mononitrate (source of vitamin b1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamin mononitrate (vitamin b1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamin mononitrate vitamin b-1": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamin mononitrate (vitamin b-1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine (vitamin b1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine hydrochloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine nitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine monitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine monoitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononirate (source of vitamin b1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrat": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (b1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (source of vitamin b)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (source of vitamin b1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b1 (thiamine mononitrate)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (vitamin b1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (vitamin b-1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (vitamin b-1) a625319": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (vitamin b-1) a625619": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (vitamin b3)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (vitamin v-1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate (vitaminb1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate source of vitamin b1": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrate vitamin b1": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitriate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiamine mononitrite": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiaminemononitrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thiaminemononitrate (vitamin b1)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"threadfin bream": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"threonine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"thyme": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"tilapia": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tilapia broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"titanium dioxide": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"titanium dioxide (color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"titanium dioxide color": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"titanium dioxide(color)": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"tocopherols (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"tofu": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"tomato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tomato concentrate": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tomato paste": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tomato paste tomato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tomato pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tomato powder": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tomato puree": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tomatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tomatopomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"tongol tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"top sirloin flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"trace": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"trace zinc oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"trace zinc proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"trace zinc sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tracezinc oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tracezinc proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zn proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tracezinc sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"trevally": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tri-calcium phosphare": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tricalcium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tri-calcium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tricalcium phsophate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tricalcium phophate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tricalciumphosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tricalicum phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"trichoderma longbrachiatum fermentation product": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"trisodium phosphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"trout": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"trout meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"tryptophan": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"tumeric": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna 60%": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna 69%": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna (source of fish)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna (source of glucosamine and chondroitin sulfate)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna (source of omega 3)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna and cod broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"tuna broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"tuna by-product": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna consomm\u00e9": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna fillet": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna fillet 30%": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna fillet 52%": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna fillet 70%": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna fillet 75%": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna fish oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"tuna fish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"tuna meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"tuna meal (preserved with ethoxyquin)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"tuna oil": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"tuna red meat": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna roe": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"tuna whole meat": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"turkey (with ground bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey and chicken broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"turkey bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey bone broth": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey breast": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"tuna by-products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"turkey by-product meal": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"turkey cartilage": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey fat": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"turkey fat (preserved with mixed tocopherols)": {
"Type": "Animal Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides essential fatty acids and energy, but should be identified (e.g., chicken fat), as unnamed sources may indicate lower quality."
},
"turkey flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"turkey giblet": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"turkey giblet liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey giblets": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"turkey giblets liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey gizzard": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey gizzards": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey hearts": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"turkey meal (a source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"turkey meal (source of chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"turkey meal (source of glucosamine and chondroitin sulfate)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"turkey meal (source of glucosamine)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"turkey necks": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey necks (source of glucosamine & chondroitin sulfate)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey peas": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"turkey powder": {
"Type": "Meat Isolates or Powder",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and often of questionable quality. May be used to increase protein content but lacks the benefits of whole meats."
},
"turkey recipe - organic turkey with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey with bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turkey with ground bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"turmeric": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"turmeric extract": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"turmeric powder": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"turmeric root": {
"Type": "Natural Colors",
"Quality": "Acceptable Quality",
"Quality Description": "Adds no nutritional value but is safer than artificial colors. Still largely unnecessary in dog food."
},
"turnip": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"turnip greens": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"type ii collagen": {
"Type": "Artificial Additives",
"Quality": "Poor Quality",
"Quality Description": "Additives like synthetic flavor enhancers or preservatives have no nutritional value and may cause long-term health issues or allergies."
},
"unsweetened apple sauce water": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"usa raised and harvested turkey meat (ground)": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"usa wild-caught smelt minnows": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"usda beef": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"usda beef liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"usda chicken": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"usda chicken liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"usda pork": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"usda pork liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"usda turkey": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"valerian root": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"veal": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"dried vegetable broth": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetable broth": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetable fat (preserved with mixed tocopherols)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"vegetable flavoring": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"vegetable glycerin": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetable juice": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetables (1%)": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetable juice (color)": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetable juice for color": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetable oil": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"vegetable oil (preserved with bha/bht)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"vegetable oil (source of linoleic acid)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"vegetable oil (source of medium-chain triglycerides)": {
"Type": "Plant Based Fat",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fatty acids, but is less biologically appropriate than animal fat for dogs. Should be used sparingly."
},
"vegetable pomace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetable pommace": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegetable starch-modified": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"vegtable broth": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"venison": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"venison blood": {
"Type": "Blood & Plasma",
"Quality": "Poor Quality",
"Quality Description": "Low-quality, heavily processed by-products used to increase protein content cheaply. Unnecessary in high-quality diets."
},
"venison bone": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venison broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"venison by-products": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"venison heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venison hearts": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venison kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venison liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venison livers": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venison lung": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venison meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"venison spleen": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venison tripe": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"venisonmmeal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"viatin d3 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vinegar": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"vinegar (preservative)": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"vital wheat gluten": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"vitame e supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin 03 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b12 (vitamin b12 supplement)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin 812 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin a": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin a acetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin a palmitate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin a supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin a (vitamin a supplement)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin aacetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin apalmitate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin asupplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b 12 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-1": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b1 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b12": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-12": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b12 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-12 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-12 supple-ment": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b12supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b2": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-2": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b2 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-3": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b5": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-5": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b5 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-6": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b6 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"(vitamin b7)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin b-7": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin bl2 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin c": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin c (ascorbic acid)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin c supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d 3 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d2 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d-2 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d3": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d-3": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d3 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d3 supple-ment": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d-3 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d3 supplement ": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d3 supplements": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d3 suppplelment": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin d3supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e ( as preservative)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e acetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e suppliment": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e supplment": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e suuplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e upplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin esupplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin k": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin k1 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin k3 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"menadione sodium busulfite complex (source of vitamin k)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin k3 supplement (menadione sodium bisulfate)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin k3 supplement (menadione sodium bisulfite)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin k3 supplement (menadione sodium bisulfite))": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin supplements": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin vitamin e supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitaminb12 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamind3 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamind3supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamine d3 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamine e (d-alpha tocopherol)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamine e supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamin e (vitamin e supplement)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamine supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamins vitamin a acetate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamins vitamin e supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamn a supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"vitamon d3 supplement": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"water": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"water (sufficient for processing)": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"water added for processing": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"water buffalo": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"water buffalo meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"water for processing": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"water suffcient for processing": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"water sufficient for cooking": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"water sufficient for processing": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"waler sufficient for processing": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"water suffient for cooking": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"watercress": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"watermelon": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"wheat": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat bran": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat flour": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat germ": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat germ meal": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat gluten": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat middling": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat middlings": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat mill run": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"rice mill run": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"wheat shorts": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheat starch": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"wheatgrass": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whey": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"whey protein concentrate": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"white fish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"white fish broth": {
"Type": "Meat Broths",
"Quality": "Poor Quality",
"Quality Description": "Often low in actual nutritional value and may contain artificial additives or excessive sodium. Should be high-quality and free from artificial flavorings."
},
"white fish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"white meal": {
"Type": "Others",
"Quality": "Poor Quality",
"Quality Description": "Undefined category; ingredients should be transparent and recognizable."
},
"white potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"white rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"white sweet potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"white vinegar": {
"Type": "Artificial Preservatives",
"Quality": "Poor Quality",
"Quality Description": "Linked to potential long-term health risks, including cancer. Common artificial preservatives include BHA, BHT, and ethoxyquin."
},
"whitebait": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whitefish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"white\ufb01sh": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whitefish (source of omega 3 and 6 fatty acids)": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whitefish meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"whitefish meal (natural source of glucosamine and chondroitin)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"whitefish meal (source of dha-docosahexaenoic acid)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"whitefish meal (source of omega 3 fatty acids)": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"white\u00ffsh meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"whiting meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"whole acadian redfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole anchovy meal": {
"Type": "Meat Meals",
"Quality": "Poor Quality",
"Quality Description": "Heavily processed, lower-quality protein source that often includes less desirable parts of animals. Lacks transparency and recognizability."
},
"whole apples": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole atlantic herring": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole atlantic mackerel": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"whole blue whiting": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole blueberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole brown rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"whole butternut squash": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole carrots": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole catfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole cell algae dried (pure source of omega 3 dha)": {
"Type": "Algae",
"Quality": "Acceptable Quality",
"Quality Description": "Algae is a natural source of omega-3s and antioxidants, beneficial in small amounts, but should be used carefully due to potential heavy metal contamination."
},
"whole chia seed": {
"Type": "Chia",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in omega-3s, fiber, and antioxidants, chia seeds are a good addition in moderation for coat health and digestion."
},
"whole chicken thighs": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole chickpeas": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"whole corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whole cranberries": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole dehydrated egg": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole dressed chicken": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole dried egg": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole dried eggs": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole dried green peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"whole dried peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"whole dried potato": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole dried potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole dried sweet potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole dry eggs": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole egg": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole egg product": {
"Type": "Meat By-Products",
"Quality": "Poor Quality",
"Quality Description": "Includes lower-quality parts of the animal (e.g., hooves, feathers), lacks transparency, and is generally less digestible and nutritious."
},
"whole eggs": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole eggs dried": {
"Type": "Whole Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Recognizable, high-quality protein source essential for muscle health and overall nutrition. Should be a primary ingredient in dog food."
},
"whole flaxseed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"whole flaxseeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"whole garlic": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole ginger": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole grain": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"whole grain barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"whole grain brown rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"whole grain corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whole grain ground corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whole grain millet": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"whole grain oatmeal": {
"Type": "Grain Meals",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and of lower nutritional value than whole grains. Often used as fillers."
},
"whole grain oats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"oat": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"whole grain rye": {
"Type": "Rye",
"Quality": "Poor Quality",
"Quality Description": "Can be hard for dogs to digest and is less nutritionally valuable compared to other grains like oats or rice. May cause digestive upset."
},
"whole grain sorghum": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"whole grain wheat": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whole green lentils": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"whole green peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"whole ground barley": {
"Type": "Barley",
"Quality": "Acceptable Quality",
"Quality Description": "Provides carbohydrates and fiber, but may be problematic for dogs with grain sensitivities. Should not be a primary ingredient."
},
"whole ground brown rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"whole ground corn": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whole ground flax seed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"whole ground flaxseed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"whole ground flaxseed meal": {
"Type": "Oilseed Meals",
"Quality": "Poor Quality",
"Quality Description": "Often low-quality by-products of the oil industry. While they provide some protein and fat, their heavy processing makes them less desirable."
},
"whole ground flaxseeds": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"whole ground millet": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"whole ground oats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"whole ground salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole ground sorghum": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"whole hake": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole herring": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole kahawai": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole lentils": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"whole mackerel": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole millet": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"whole navy beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"whole oat groats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"whole oat meal": {
"Type": "Grain Meals",
"Quality": "Poor Quality",
"Quality Description": "Highly processed and of lower nutritional value than whole grains. Often used as fillers."
},
"whole oats": {
"Type": "Oats",
"Quality": "Acceptable Quality",
"Quality Description": "Provides fiber and is generally safe for dogs with grain sensitivities. A good alternative to other grains like wheat or corn."
},
"whole parsley": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"whole parsnips": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole pears": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"whole perch": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole pilchard": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole pinto beans": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"whole potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole pumpkin": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole rabbit (with bone)": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"whole red lentils": {
"Type": "Legumes",
"Quality": "Poor Quality",
"Quality Description": "Linked to increased risk of DCM (dilated cardiomyopathy) in dogs when used as a primary protein source, especially in grain-free diets."
},
"redfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole redfish": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"whole sardines": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole sorghum": {
"Type": "Sorghum",
"Quality": "Acceptable Quality",
"Quality Description": "Gluten-free and rich in nutrients, but should be a secondary ingredient to high-quality animal proteins."
},
"whole southern blue whiting": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole spelt": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whole sweet potatoes": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole wheat": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whole wheat flour": {
"Type": "Wheat, Corn, Soy",
"Quality": "Poor Quality",
"Quality Description": "Common allergens in dogs and often used as cheap fillers. These ingredients can contribute to food sensitivities and digestive upset."
},
"whole wheat macaroni": {
"Type": "Human Food Ingredients",
"Quality": "Acceptable Quality",
"Quality Description": "As long as they are safe for dogs and meet nutritional needs, human-grade ingredients can be a high-quality choice. Transparency is key."
},
"whole white trevally": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"whole yams": {
"Type": "Fruits & Vegetables",
"Quality": "Acceptable Quality",
"Quality Description": "Rich in fiber, vitamins, and antioxidants. Whole, recognizable fruits and vegetables are ideal, especially for digestive health."
},
"whole yellow peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"whole zucchini": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"wholeflaxseed": {
"Type": "Oilseeds",
"Quality": "Acceptable Quality",
"Quality Description": "Provide omega-3s and healthy fats but should be used in moderation and sourced from safe, high-quality plants."
},
"wild alaskan salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"wild boar": {
"Type": "Meats",
"Quality": "Acceptable Quality",
"Quality Description": "Whole, identifiable meats are the highest-quality protein sources for dogs and should be a primary ingredient."
},
"boar heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"boar kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"boar spleen": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"wild boar cartilage": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"wild boar heart": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"wild boar kidney": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"wild boar liver": {
"Type": "Organ Parts",
"Quality": "Acceptable Quality",
"Quality Description": "Organ meats like liver and heart are nutrient-dense, offering essential vitamins, minerals, and amino acids, but should not dominate the diet due to high vitamin A."
},
"wild caught salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"wild rice": {
"Type": "Rice",
"Quality": "Acceptable Quality",
"Quality Description": "Provides easily digestible carbohydrates and energy, but should be balanced with high-quality proteins. Suitable for sensitive stomachs."
},
"wild salmon": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"wild-caught shrimp": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"wild-caught yellowfin tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"wood-grilled chicken flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"xantham gum": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"xanthan": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"xanthan gum": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"xanthn gum": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"xathan gum": {
"Type": "Natural Preservatives",
"Quality": "Acceptable Quality",
"Quality Description": "Safer and less likely to cause allergies than artificial preservatives. Look for tocopherols (Vitamin E) or rosemary extract."
},
"yeast": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast culture": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast culture (probiotic)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast culture (saccharomyces cerevisiae)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast cultures": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast extract": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast extract (a source of prebiotics)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast extract (source of mannan-oligosaccharides)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast flavor": {
"Type": "Natural Flavors",
"Quality": "Poor Quality",
"Quality Description": "\"Natural\" flavors can lack transparency and may come from questionable sources. Avoid unless the source is clearly identified and reputable."
},
"yeast hydrolysate (source of beta-glucans)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yeast hydrolysate (source of _x0003_beta-glucans)": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yellow #5": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"yellow #6": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"yellow 5": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"yellow 6": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"yellow 6 lake": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"yellow iron oxide": {
"Type": "Artificial Colors",
"Quality": "Poor Quality",
"Quality Description": "Unnecessary, non-nutritive, and associated with potential allergic reactions or hyperactivity in dogs."
},
"yellow peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"yellow split peas": {
"Type": "Peas",
"Quality": "Poor Quality",
"Quality Description": "Linked to an increased risk of DCM in some dogs when used as a primary ingredient. Should be limited, especially in grain-free diets."
},
"yellowfin tuna": {
"Type": "Fish Meats",
"Quality": "Acceptable Quality",
"Quality Description": "High-quality source of omega-3 fatty acids and protein, but should be from identifiable species to avoid contamination (e.g., mercury)."
},
"yogurt": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"yogurt cultures": {
"Type": "Enzymes & Probiotics",
"Quality": "Acceptable Quality",
"Quality Description": "Promotes digestive health and nutrient absorption, contributing to overall gut health."
},
"yogurt whey": {
"Type": "Dairy Products",
"Quality": "Poor Quality",
"Quality Description": "Many dogs are lactose intolerant, leading to digestive upset. Should be used sparingly and from quality sources (e.g., yogurt, cheese) if included."
},
"yucca": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca schdigera extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca schidegera": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca schidegera extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca schidigera": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca schidigera extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca schidigera extract (probiotic)": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca schidigeraextract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca schidicera extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"yucca shidigera extract": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"zedoary": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
},
"zin proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zin sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc amino acid  chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc amino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc amino acid complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc amino acid complex (chelate)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc amino acidchelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc gluconate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc glycine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc hydroxychloride": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc methionine": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc methionine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc methionine hydroxy analogue chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc oxide": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc polysaccharide complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc protein": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc proteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc proteinate (source of chelated zinc)": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc sulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc sulfate heptahydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc sulfate monohydrate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc sulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc suplhate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zincamino acid chelate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zincmethionine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zinc-methionine complex": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zincproteinate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zincsulfate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zincsulphate": {
"Type": "Supplement",
"Quality": "Acceptable Quality",
"Quality Description": "Can be beneficial when targeted at specific deficiencies, but should be used in moderation and sourced from high-quality providers."
},
"zucchini": {
"Type": "Natural Additives",
"Quality": "Acceptable Quality",
"Quality Description": "When derived from recognizable, safe sources, these additives can enhance nutritional value (e.g., vitamins, minerals)."
}
}