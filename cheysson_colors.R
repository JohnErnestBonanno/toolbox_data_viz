library(ggplot2)
library(ggCheysson)

ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
  geom_point(size = 3) +
  scale_color_cheysson("1881_22") + #where teh color goes
  labs(title = "Iris Dataset") +
  theme_minimal()


show_palettes(list_cheysson_pals()$name, ncol = 5)


for (pal in list_cheysson_pals()$name) {
  show_palette(pal)
}