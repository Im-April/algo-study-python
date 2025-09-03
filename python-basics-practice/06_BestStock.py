def best_stock(data) :
    max_price = 0
    answer = ''

    for s in data :
        if data[s] > max_price:
            max_price = data[s]
            answer = s

    return answer


stocks = {
    'AAPL': 135.5,
    'GOOG': 2729.3,
    'MSFT': 289.5
}

print(best_stock(stocks))
