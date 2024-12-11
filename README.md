# lowEloEngine

**This engine is made for simplicity over efficiency. For that reason, this bot will not look 10, 15... moves ahead like many top engines, including but not limited to StockFish, Lc0, and Mittens.**

This is a chess client in which I have built my bot around, just for simplicities sake. Therefor this bot has no implementation with Lichess Bot API, or compatability with chess bot GUIs like Cute Chess or Arena Chess GUI.

The 'main' branch has a custom made chess client, completely from scratch and not using a library such as python-chess. One reason for this is so that I can learn how chess for another project, and because I want to, and feel it would be a good exercise, as well as at least for me easier engine implementation.

Currently, once a pawn reaches the end of the board, it is automatically made a Queen. I will be working on a way to select which piece to promote to.