# あなたの借金は大丈夫ですか？  
[![test](https://github.com/N-Reon/robosys2024/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/N-Reon/robosys2024/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)  

## 概要  
このプログラムは10万円を年利18%で借りたときの  
1日ごとの利息を出力するROS2のパッケージです。  
## ノード  

## トピック  

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

## ライセンス
このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
このコマンドは以下のサイトを参考にしています。
https://www.aiful.co.jp/cardloan/interest-rates-overview/  
© 2024 Reon Nukui  

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7 ~ 3.11  
 
## テスト環境
- Ubuntu 22.04 LTS

