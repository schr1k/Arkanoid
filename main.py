import io
import pygame
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit, QApplication
import sys
from PyQt5 import uic


def draw(screen):
    screen.fill((200, 200, 200))
    font = pygame.font.Font(None, 50)
    text_arcanoid = font.render("Арканоид", True, (255, 0, 0))
    text_arcanoid_x = width // 2 - text_arcanoid.get_width() // 2
    text_arcanoid_y = height // 3 - text_arcanoid.get_height() // 3
    text_arcanoid_w = text_arcanoid.get_width()
    text_arcanoid_h = text_arcanoid.get_height()
    screen.blit(text_arcanoid, (text_arcanoid_x, text_arcanoid_y))
    pygame.draw.rect(screen, (255, 0, 0), (text_arcanoid_x - 10, text_arcanoid_y - 10,
                                           text_arcanoid_w + 20, text_arcanoid_h + 20), 1)

    font1 = pygame.font.Font(None, 50)
    text_press = font.render("Нажмите на любую кнопку для продолжения", True, (255, 0, 0))
    text_press_x = width // 2 - text_press.get_width() // 2
    text_press_y = height // 6 * 3 - text_press.get_height() // 6 * 3
    text_press_w = text_press.get_width()
    text_press_h = text_press.get_height()
    screen.blit(text_press, (text_press_x, text_press_y))
    pygame.draw.rect(screen, (255, 0, 0), (text_press_x - 10, text_press_y - 10,
                                           text_press_w + 20, text_press_h + 20), 1)


class NickName(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('nickname_input.ui', self)
        self.setWindowTitle('Арканоид')
        self.pushButton.clicked.connect(self.load_nickname_in_db)

    def load_nickname_in_db(self):
        self.nickname = self.lineEdit.text()
        print(self.nickname)
        self.close()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Арканоид')
    app = QApplication(sys.argv)
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    draw(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                ex = NickName()
                ex.show()
        pygame.display.flip()
    pygame.quit()
