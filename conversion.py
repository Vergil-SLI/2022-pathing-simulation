class Conversion:
    def __init__(self, screen_width, screen_height, field_width, field_height):
        self.conversion_factor = (field_width/screen_width + field_height/screen_height) / 2


    def pixel_to_meter(self, pixel):
        return pixel * self.conversion_factor

    def meter_to_pixel(self, meter):
        return meter / self.conversion_factor
