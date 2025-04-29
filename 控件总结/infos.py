import sys
import random
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from qfluentwidgets import NavigationItemPosition, FluentWindow, SplashScreen, setTheme, Theme, MSFluentWindow, \
    SubtitleLabel, setFont, FluentIcon


class SnakeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initGame()
        self.setFixedSize(600, 400)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 0.8)")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.gameLoop)
        self.timer.start(150)
        self.score = 0

    def initGame(self):
        self.snake = [[100, 100], [80, 100], [60, 100]]
        self.food = self.generateFood()
        self.direction = 'Right'
        self.next_direction = 'Right'
        self.game_active = True

    def generateFood(self):
        while True:
            x = random.randint(0, 29) * 20
            y = random.randint(0, 19) * 20
            if [x, y] not in self.snake:
                return [x, y]

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawSnake(painter)
        self.drawFood(painter)
        self.drawScore(painter)
        if not self.game_active:
            self.drawGameOver(painter)

    def drawSnake(self, painter):
        painter.setBrush(QColor(40, 167, 69))
        for segment in self.snake:
            painter.drawRect(segment[0], segment[1], 18, 18)

    def drawFood(self, painter):
        painter.setBrush(QColor(220, 53, 69))
        painter.drawEllipse(self.food[0], self.food[1], 18, 18)

    def drawScore(self, painter):
        painter.setFont(QFont('Segoe UI', 12))
        painter.setPen(QColor(0, 0, 0))
        painter.drawText(10, 20, f"Score: {self.score}")

    def drawGameOver(self, painter):
        painter.setFont(QFont('Segoe UI', 24, QFont.Bold))
        painter.setPen(QColor(220, 53, 69))
        painter.drawText(self.rect(), Qt.AlignCenter, "Game Over!")

    def keyPressEvent(self, event):
        key = event.key()
        directions = {
            Qt.Key_Up: 'Up',
            Qt.Key_Down: 'Down',
            Qt.Key_Left: 'Left',
            Qt.Key_Right: 'Right'
        }
        if key in directions:
            self.next_direction = directions[key]

    def validateDirection(self):
        opposites = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
        if opposites[self.direction] != self.next_direction:
            self.direction = self.next_direction

    def moveSnake(self):
        head = self.snake[0].copy()
        if self.direction == 'Right':
            head[0] += 20
        elif self.direction == 'Left':
            head[0] -= 20
        elif self.direction == 'Up':
            head[1] -= 20
        elif self.direction == 'Down':
            head[1] += 20

        if self.checkCollision(head):
            self.game_active = False
            return

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 10
            self.food = self.generateFood()
        else:
            self.snake.pop()

    def checkCollision(self, head):
        x, y = head
        if (x < 0 or x >= 600 or y < 0 or y >= 400):
            return True
        if head in self.snake[1:]:
            return True
        return False

    def gameLoop(self):
        if self.game_active:
            self.validateDirection()
            self.moveSnake()
            self.update()

class GameWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()
        setTheme(Theme.DARK)
        self.setWindowTitle("Fluent Snake Game")
        self.setMinimumSize(700, 500)

        self.game = SnakeGame()
        self.addSubInterface(self.game, 'game', 'Snake Game')

        # Add score label
        self.scoreLabel = SubtitleLabel('Score: 0', self)
        setFont(self.scoreLabel, 14)
        self.scoreLabel.move(620, 20)
        self.game.scoreChanged = lambda: self.scoreLabel.setText(f"Score: {self.game.score}")

        # Update score display
        self.game.scoreChanged = self.updateScore

    def updateScore(self):
        self.scoreLabel.setText(f"Score: {self.game.score}")

    def keyPressEvent(self, event):
        self.game.keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 使用简单启动方式
    window = GameWindow()
    window.show()

    sys.exit(app.exec_())