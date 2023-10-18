# Configuration

`rich-click` adheres to the following lookup order when searching through sources for configuration values (the first source is always applied first, the second source is applied second, etc.):

1. The help config directly passed to the `RichCommand`.
2. The help config of a parent command.
3. Globals in `rich_click.rich_click`.
