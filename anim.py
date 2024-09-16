import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Dot-Based Chemical Nanosensors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)
explanation_font = pygame.font.Font(None, 20)

# Scene variables
current_scene = 0
scene_timer = 0
scene_duration = 15000  # 15 seconds per scene

# Interactive elements
particles = []

class QuantumDot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.color = YELLOW

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

class Analyte:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = RED

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(2, 5)
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            self.angle = random.uniform(0, 2 * math.pi)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)

quantum_dot = QuantumDot(width // 2, height // 2)
analyte = Analyte(width // 4, height // 2)

def create_particles(num):
    return [Particle(random.randint(0, width), random.randint(0, height)) for _ in range(num)]

def draw_gradient_background(color1, color2):
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)
        pygame.draw.line(screen, (r, g, b), (0, y), (width, y))

def draw_wrapped_text(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        if y + fontHeight > rect.bottom:
            break

        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        text = text[i:]

    return text

def draw_scene_0():
    draw_gradient_background(PURPLE, BLUE)
    for particle in particles:
        particle.move()
        particle.draw(screen)
    
    text = font.render("Quantum Dot-Based Chemical Nanosensors", True, WHITE)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    
    explanation = "Quantum dots are nanoscale semiconductors that exhibit unique optical and electronic properties. When used as chemical nanosensors, they can detect specific molecules with high sensitivity and selectivity."
    draw_wrapped_text(screen, explanation, WHITE, (50, height - 150, width - 100, 100), explanation_font)

def draw_scene_1():
    draw_gradient_background(BLUE, LIGHT_BLUE)
    
    text = font.render("CdS Quantum Dot Preparation (Microemulsion)", True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, 50))
    
    pygame.draw.circle(screen, WHITE, (width // 2, height // 2), 100)  # Water droplet
    pygame.draw.circle(screen, YELLOW, (width // 2, height // 2), 20)  # CdS quantum dot
    
    text = small_font.render("Water droplet", True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 + 120))
    text = small_font.render("CdS quantum dot", True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 60))
    
    explanation = "Microemulsion is a method used to synthesize CdS quantum dots. Tiny water droplets in oil act as nanoreactors, where cadmium and sulfur precursors react to form CdS nanocrystals with controlled size and properties."
    draw_wrapped_text(screen, explanation, BLACK, (50, height - 150, width - 100, 100), explanation_font)

def draw_scene_2():
    draw_gradient_background(BLACK, PURPLE)
    
    text = font.render("Quantum Dot Fluorescence", True, WHITE)
    screen.blit(text, (width // 2 - text.get_width() // 2, 50))
    
    quantum_dot.draw(screen)
    
    # Draw fluorescence
    for i in range(8):
        angle = i * math.pi / 4
        end_x = quantum_dot.x + math.cos(angle) * 100
        end_y = quantum_dot.y + math.sin(angle) * 100
        pygame.draw.line(screen, GREEN, (quantum_dot.x, quantum_dot.y), (end_x, end_y), 2)
    
    explanation = "Quantum dots exhibit fluorescence when excited by light. They absorb photons of higher energy and emit photons of lower energy. The emission wavelength depends on the size of the quantum dot, allowing for tunable optical properties."
    draw_wrapped_text(screen, explanation, WHITE, (50, height - 150, width - 100, 100), explanation_font)

def draw_scene_3():
    draw_gradient_background(LIGHT_BLUE, WHITE)
    
    text = font.render("Analyte Detection", True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, 50))
    
    quantum_dot.draw(screen)
    analyte.draw(screen)
    
    # Draw arrow
    pygame.draw.line(screen, BLACK, (analyte.x + 20, analyte.y), (quantum_dot.x - 30, quantum_dot.y), 2)
    pygame.draw.polygon(screen, BLACK, [(quantum_dot.x - 30, quantum_dot.y - 5), (quantum_dot.x - 20, quantum_dot.y), (quantum_dot.x - 30, quantum_dot.y + 5)])
    
    explanation = "When an analyte (target molecule) interacts with the quantum dot, it can change the dot's fluorescence properties. This change can be detected and quantified, allowing for sensitive and specific chemical sensing."
    draw_wrapped_text(screen, explanation, BLACK, (50, height - 150, width - 100, 100), explanation_font)

def draw_scene_4():
    draw_gradient_background(PURPLE, BLACK)
    
    text = font.render("Quantum Confinement Effect", True, WHITE)
    screen.blit(text, (width // 2 - text.get_width() // 2, 50))
    
    # Draw energy levels
    pygame.draw.rect(screen, BLUE, (200, 200, 400, 200))
    pygame.draw.line(screen, WHITE, (250, 250), (350, 250), 2)
    pygame.draw.line(screen, WHITE, (450, 350), (550, 350), 2)
    
    # Draw arrows
    pygame.draw.line(screen, GREEN, (300, 350), (300, 270), 3)
    pygame.draw.polygon(screen, GREEN, [(295, 270), (300, 260), (305, 270)])
    
    text = small_font.render("Conduction Band", True, WHITE)
    screen.blit(text, (570, 245))
    text = small_font.render("Valence Band", True, WHITE)
    screen.blit(text, (570, 345))
    text = small_font.render("Excitation", True, WHITE)
    screen.blit(text, (310, 300))
    
    explanation = "The quantum confinement effect occurs when the size of a semiconductor nanocrystal is smaller than its exciton Bohr radius. This confinement leads to discrete energy levels and size-dependent optical and electronic properties."
    draw_wrapped_text(screen, explanation, WHITE, (50, height - 150, width - 100, 100), explanation_font)

def draw_scene_5():
    draw_gradient_background(BLUE, GREEN)
    
    text = font.render("Size-Dependent Optical Properties", True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, 50))
    
    # Draw quantum dots of different sizes
    pygame.draw.circle(screen, RED, (200, 300), 30)
    pygame.draw.circle(screen, ORANGE, (400, 300), 20)
    pygame.draw.circle(screen, YELLOW, (600, 300), 10)
    
    text = small_font.render("Larger QD", True, BLACK)
    screen.blit(text, (170, 350))
    text = small_font.render("Medium QD", True, BLACK)
    screen.blit(text, (370, 350))
    text = small_font.render("Smaller QD", True, BLACK)
    screen.blit(text, (570, 350))
    
    text = small_font.render("Lower Energy", True, BLACK)
    screen.blit(text, (170, 400))
    text = small_font.render("Medium Energy", True, BLACK)
    screen.blit(text, (370, 400))
    text = small_font.render("Higher Energy", True, BLACK)
    screen.blit(text, (570, 400))
    
    explanation = "The size of a quantum dot directly affects its optical properties. Smaller quantum dots emit higher energy (shorter wavelength) light, while larger quantum dots emit lower energy (longer wavelength) light. This allows for precise tuning of emission color."
    draw_wrapped_text(screen, explanation, BLACK, (50, height - 150, width - 100, 100), explanation_font)

def draw_scene_6():
    draw_gradient_background(ORANGE, YELLOW)
    
    text = font.render("Surface Functionalization", True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, 50))
    
    # Draw quantum dot
    pygame.draw.circle(screen, RED, (width // 2, height // 2), 50)
    
    # Draw functional groups
    for i in range(12):
        angle = i * math.pi / 6
        end_x = width // 2 + math.cos(angle) * 70
        end_y = height // 2 + math.sin(angle) * 70
        pygame.draw.circle(screen, BLUE, (int(end_x), int(end_y)), 10)
    
    text = small_font.render("Quantum Dot Core", True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 + 70))
    text = small_font.render("Functional Groups", True, BLACK)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 90))
    
    explanation = "Surface functionalization involves attaching specific molecules to the quantum dot surface. This can enhance stability, solubility, and biocompatibility. It also allows for targeted sensing by attaching molecules that interact specifically with the analyte of interest."
    draw_wrapped_text(screen, explanation, BLACK, (50, height - 150, width - 100, 100), explanation_font)

def main():
    global current_scene, scene_timer, particles
    
    clock = pygame.time.Clock()
    particles = create_particles(50)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_scene = (current_scene + 1) % 7
                scene_timer = pygame.time.get_ticks()
        
        # Update scene
        current_time = pygame.time.get_ticks()
        if current_time - scene_timer > scene_duration:
            current_scene = (current_scene + 1) % 7
            scene_timer = current_time
        
        # Draw current scene
        if current_scene == 0:
            draw_scene_0()
        elif current_scene == 1:
            draw_scene_1()
        elif current_scene == 2:
            draw_scene_2()
        elif current_scene == 3:
            draw_scene_3()
        elif current_scene == 4:
            draw_scene_4()
        elif current_scene == 5:
            draw_scene_5()
        elif current_scene == 6:
            draw_scene_6()
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()