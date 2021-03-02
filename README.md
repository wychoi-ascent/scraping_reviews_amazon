# scraping_reviews_amazon

## Settings

### Make virtual environment
```
python -m venv venv
```

### Activate virtual environment
```
venv\Scripts\activate
```

### Download all libraries
```
pip install -r requirements.txt
```

## Operation

### Start scraping reviews
```
cd amazon_reviews_scraping\spiders
scrapy runspider amazon_review.py -o reviews.csv
```

### Analyze reviews by ratings
```
python analyzer.py
```
