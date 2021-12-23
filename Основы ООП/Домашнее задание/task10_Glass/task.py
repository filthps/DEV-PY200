class Glass:
    def __init__(self, material):
        self.material = material

    def get_material(self):
        return self.material


if __name__ == "__main__":
    g = Glass("r")
    print(g.get_material())
