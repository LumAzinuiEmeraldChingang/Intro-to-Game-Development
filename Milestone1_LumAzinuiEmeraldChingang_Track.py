import pygame

pygame.init()

# -------------------------
# WINDOW
# -------------------------
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lum Azinui Emerald Chingang's Window")

clock = pygame.time.Clock()

# -------------------------
# PLAYER SETTINGS
# -------------------------
x = 100
y = 300
speed = 300

facing_right = True

# -------------------------
# ANIMATION SETTINGS
# -------------------------
frame_surfaces = []
TOTAL_FRAMES = 4  # Change if you add more images

for i in range(TOTAL_FRAMES):
    image = pygame.image.load(f"{i}.png").convert_alpha()
    frame_surfaces.append(image)

frame_count = len(frame_surfaces)
frame = 0
timer = 0
frame_duration = 0.1

# -------------------------
# MAIN LOOP
# -------------------------
running = True
while running:
    delta_time = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False

    # -------------------------
    # MOVEMENT
    # -------------------------
    if keys[pygame.K_RIGHT]:
        x += speed * delta_time
        facing_right = False
        moving = True

    if keys[pygame.K_LEFT]:
        x -= speed * delta_time
        facing_right = True
        moving = True

    if keys[pygame.K_UP]:      # forward
        y -= speed * delta_time
        moving = True

    if keys[pygame.K_DOWN]:    # backward
        y += speed * delta_time
        moving = True
# MOVEMENT (your arrow key code here)

# ---- ADD BOUNDARY LIMITS HERE ----
    char_width = frame_surfaces[0].get_width()
    char_height = frame_surfaces[0].get_height()

    if x < 0:
        x = 0
    if x > width - char_width:
        x = width - char_width

    if y < 0:
        y = 0
    if y > height - char_height:
       y = height - char_height

    # -------------------------
    # ANIMATION
    # -------------------------
    if moving:
        timer += delta_time
        if timer >= frame_duration:
            frame = (frame + 1) % frame_count
            timer = 0
    else:
        frame = 0  # idle frame

    # -------------------------
    # DRAW
    # -------------------------
    screen.fill((210, 0, 210))

    current_image = frame_surfaces[frame]

    # Flip image when facing left
    if not facing_right:
        current_image = pygame.transform.flip(current_image, True, False)

    screen.blit(current_image, (x, y))

    pygame.display.flip()

pygame.quit()