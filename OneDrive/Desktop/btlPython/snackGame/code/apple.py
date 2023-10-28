from settings import * 
from random import choice
from math import sin

class Apple:
	def __init__(self, snake):
		self.pos = pygame.Vector2()  # Tạo một đối tượng Vector2 để lưu trữ tọa độ của quả táo
		self.display_surface = pygame.display.get_surface()  # Lấy bề mặt hiển thị của pygame
		self.snake = snake  # Tham chiếu đến đối tượng rắn (Snake)
		self.set_pos()  # Gọi hàm set_pos() để đặt vị trí ban đầu của quả táo

		self.surf = pygame.image.load(join('..', 'graphics', 'apple.png')).convert_alpha()  # Tải hình ảnh quả táo từ tệp tin và chuyển đổi alpha
		self.scaled_surf = self.surf.copy()  # Sao chép hình ảnh quả táo 
		self.scaled_rect = self.scaled_surf.get_rect(
			center = (self.pos.x * CELL_SIZE + CELL_SIZE / 2, self.pos.y * CELL_SIZE + CELL_SIZE / 2))  # Đặt kích thước và vị trí ban đầu của quả táo trên màn hình

	def set_pos(self):
    	# Tạo danh sách các vị trí có sẵn để đặt quả táo, tránh đặt trên cơ thể của rắn
		available_pos = [pygame.Vector2(x, y) for x in range(COLS) for y in range(ROWS) 
			 if pygame.Vector2(x, y) not in self.snake.body]  
		self.pos = choice(available_pos)  # Chọn một vị trí ngẫu nhiên từ danh sách các vị trí có sẵn để đặt quả táo

	def draw(self):
		self.scaled_rect = self.scaled_surf.get_rect(
			center = (self.pos.x * CELL_SIZE + CELL_SIZE / 2, self.pos.y * CELL_SIZE + CELL_SIZE / 2))  # Cập nhật vị trí 
		self.display_surface.blit(self.scaled_surf, self.scaled_rect)  # Vẽ quả táo lên màn hình
