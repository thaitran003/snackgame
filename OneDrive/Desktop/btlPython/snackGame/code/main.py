# khai báo các 
from settings import * 
from snake import Snake
from apple import Apple

class Main:
	def __init__(self):
		# Tạo cửa sổ trò chơi với kích thước và tiêu đề 
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
		pygame.display.set_caption('Ran san moi')

		# Tạo danh sách bg_rects chứa các hình chữ nhật để tạo lưới ô vuông cho nền trò chơi.
		self.bg_rects = [pygame.Rect(
			(col + int(row % 2 == 0)) * CELL_SIZE,  # Tọa độ x của hình chữ nhật
			row * CELL_SIZE,                         # Tọa độ y của hình chữ nhật
			CELL_SIZE, CELL_SIZE)                    # Kích thước (width và height) của hình chữ nhật
			for col in range(0, COLS, 2)             # Lặp qua các cột (chỉ cột chẵn)
			for row in range(ROWS)]                  # Lặp qua tất cả các hàng
		self.snake = Snake()
		self.apple = Apple(self.snake)

		# timer 
		self.update_event = pygame.event.custom_type()
		pygame.time.set_timer(self.update_event, 200)
		self.game_active = False

		# âm thanh cho trò chơi: âm thanh khi ăn quả táo và âm thanh nền.
		self.crunch_sound = pygame.mixer.Sound(join('..', 'audio', 'crunch.wav'))
		self.bg_music = pygame.mixer.Sound(join('..', 'audio', 'arcade.ogg'))
		self.bg_music.set_volume(0.5)
		self.bg_music.play(-1)

	def draw_bg(self):
		self.display_surface.fill(LIGHT_GREEN)
		for rect in self.bg_rects:
			pygame.draw.rect(self.display_surface, DARK_GREEN, rect)

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]: 
			self.snake.direction = pygame.Vector2(1,0) if self.snake.direction.x != -1 else self.snake.direction
		if keys[pygame.K_LEFT]: 
			self.snake.direction = pygame.Vector2(-1,0) if self.snake.direction.x != 1 else self.snake.direction
		if keys[pygame.K_UP]: 
			self.snake.direction = pygame.Vector2(0,-1) if self.snake.direction.y != 1 else self.snake.direction
		if keys[pygame.K_DOWN]: 
			self.snake.direction = pygame.Vector2(0,1) if self.snake.direction.y != -1 else self.snake.direction
   
	# va cham 
	def collision(self):
		# va cham qua tao 
		if self.snake.body[0] == self.apple.pos:
			self.snake.has_eaten = True
			self.apple.set_pos()
			self.crunch_sound.play()

		# game over 
		if self.snake.body[0] in self.snake.body[1:] or \
			not 0 <= self.snake.body[0].x < COLS or \
			not 0 <= self.snake.body[0].y < ROWS:
			self.snake.reset()
			self.game_active = False

	def draw_shadow(self):
		# Tạo một bề mặt mới với màu xanh lam và xác định màu nền trong bề mặt đó
		shadow_surf = pygame.Surface(self.display_surface.get_size())
		shadow_surf.fill((0, 255, 0))
		shadow_surf.set_colorkey((0, 255, 0))
		
		# Vẽ bề mặt táo và rắn lên bề mặt shadow
		shadow_surf.blit(self.apple.scaled_surf, self.apple.scaled_rect.topleft + SHADOW_SIZE)
		for surf, rect in self.snake.draw_data:
			shadow_surf.blit(surf, rect.topleft + SHADOW_SIZE)

		# Tạo một mask dựa trên bề mặt shadow
		mask = pygame.mask.from_surface(shadow_surf)
		# Đảo ngược mask (đổi màu nền thành màu đục và ngược lại)
		mask.invert()
		# Chuyển mask thành bề mặt để tạo bóng
		shadow_surf = mask.to_surface()
		# Đặt màu nền trong bề mặt shadow
		shadow_surf.set_colorkey((255, 255, 255))
		# Đặt độ mờ (độ trong suốt) cho bề mặt shadow
		shadow_surf.set_alpha(SHADOW_OPACITY)

		# Vẽ bề mặt shadow lên màn hình
		self.display_surface.blit(shadow_surf, (0, 0))


	def run(self):
		while True:
			# Xử lý sự kiện
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

				if event.type == self.update_event and self.game_active:
					self.snake.update()

				if event.type == pygame.KEYDOWN and not self.game_active:
					# Bắt đầu trò chơi khi người chơi ấn một phím
					self.game_active = True

			# Cập nhật trạng thái
			self.input()  # Xử lý đầu vào người chơi
			self.collision()  # Kiểm tra va chạm

			# Vẽ màn hình
			self.draw_bg()  # Vẽ nền
			self.draw_shadow()  # Vẽ bóng 
			self.snake.draw()  # Vẽ rắn
			self.apple.draw()  # Vẽ quả táo
			pygame.display.update()  # Cập nhật màn hình

if __name__ == '__main__':
	main = Main()
	main.run()