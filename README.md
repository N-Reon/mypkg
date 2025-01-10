# 利息計算  
[![test](https://github.com/N-Reon/mypkg/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/N-Reon/mypkg/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)  
## 概要  
このプログラムはROS 2のパッケージです。  
送信側と受信側の2つの端末を使用します。  
listener.pyはテスト用に残してあります。  
  
## ノード  
- ノード名 : interest  
- 10万円を年利18%で借りたときの1日ごとの利息を送信します。 
 
## トピック  
- トピック名 : kane  
- 1秒を1日としています。  
- 1秒間隔で利息を受信します。  

## 実行例
- 送信側
```bash  
$ ros2 run mypkg interest  
```  

- 受信側  
```bash  
$ ros2 topic echo /kane  
```  

- 受信側実行例  
```bash
$ ros2 topic echo /kane
data: 147.0
---
data: 197.0
---
data: 246.0
---
data: 295.0
---
data: 394.0
---
data: 443.0
---
data: 493.0
---
data: 542.0
---
```

## 参考サイト
- このコマンドは以下のサイトを参考にしています。  
https://www.aiful.co.jp/cardloan/interest-rates-overview/  

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.10  

- テストに利用したコンテナ  
  - https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2  
 
## テスト環境
- Ubuntu 20.04 LTS
- ROS 2 foxy

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。  
- © 2024 Reon Nukui
