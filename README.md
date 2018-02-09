# Anotações

* Seed / Load Data
1. Criar pasta **fixture** (reconhecida pelo pyton evitando a necessidade de colocar o caminho absoluto) 
2. **Python manage.py loaddata data.json**
3. Se pasta for incluída em outros níveis, incluir no arquivo **settings.py** a config **FIXTURE_DIRS=('templates')**

* Dump Data
1. Banco para arquivo: **python manage.py dumpdata --output ./dumpdata.json --exclude=contenttypes --exclude=auth**
