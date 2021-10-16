# Ryu

1. Dijkstra.py

    透過Dijkstra演算法來於SDN中執行最短路由，此處每條路權重預設為1。
    
2. Dijkstra_bw.py

    承接project1，透過端口監控來取得每一條鏈路當前使用的頻寬，並以剩餘最大的頻寬量作為路由依據。此處請先準備一個bw.txt來導入初始的頻寬值。
    Note:因為需要取值當前的頻寬才能進行路由，所以在mininet執行時，需要稍等片刻直到update bandwidth出現時，才能開始進行路由。
    
3. Dijkstra_delay.py

    承接Project1，根據最小的delay來進行路由規劃。
    Note:因為需要取值當前的頻寬才能進行路由，所以在mininet執行時，需要稍等片刻直到update bandwidth出現時，才能開始進行路由。
