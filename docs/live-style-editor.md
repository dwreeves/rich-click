# Live Style Editor

<style>
    .rc-button.button-selected code {
      background-color: #00ffff;
    }
    .rc-element.c-red {
        color: #CC3333;
    }
    .rc-element.c-blue {
        color: #2277DD;
    }
    .rc-element.c-green {
        color: #33AA33;
    }
    .rc-element.s-italic {
        font-style: italic;
    }
    .rc-element.s-bold {
        font-weight: bold;
    }
    .rc-element.s-dim {
        opacity: 75%;
    }
</style>
<div>
    <label for="color-select">`STYLE_OPTION`:</label>
    <select id="color-select" onchange="changeColor('rccfg-style-option')">
        <option value="">(none)</option>
        <option value="c-red">red</option>
        <option value="c-blue">blue</option>
        <option value="c-green">green</option>
    </select>
    <button class="rc-button rccfg-style-option rcstyle-dim"><code>dim</code></button>
    <button class="rc-button rccfg-style-option rcstyle-bold"><code>bold</code></button>
    <button class="rc-button rccfg-style-option rcstyle-italic"><code>italic</code></button>
</div>
<script>document.getElementById("color-select").selectedIndex = 0;</script>

<script>
    // I am not good at Javascript. :(
    // If you see this message and are better at Javascript than me, consider lending me a hand! :)

    const rcStyleButtons = document.querySelectorAll('button.rc-button');

    rcStyleButtons.forEach(rcStyleButton => {
        rcStyleButton.addEventListener('click', function() {
            const rccfgSelection = Array.from(rcStyleButton.classList).find(className => className.startsWith('rccfg-'));
            const rcstyleSelection = Array.from(rcStyleButton.classList).find(className => className.startsWith('rcstyle-'));

            if (rcStyleButton.classList.contains('button-selected')) {
                // turning off
                rcStyleButton.classList.remove('button-selected');
                toggleStyle(rccfgSelection, rcstyleSelection, false);
            } else {
                // turning on
                rcStyleButton.classList.add('button-selected');
                toggleStyle(rccfgSelection, rcstyleSelection, true);
            }
        });
    });

    function toggleStyle(cfg, style, enable) {
        const allSpans = document.querySelectorAll('span.'.concat(cfg));
        allSpans.forEach(element => {
            if (style == 'rcstyle-italic') {
                if (enable) {
                    element.classList.add('s-italic');
                } else {
                    element.classList.remove('s-italic');
                }
            } else if (style == 'rcstyle-bold') {
                if (enable) {
                    element.classList.add('s-bold');
                } else {
                    element.classList.remove('s-bold');
                }
            } else if (style == 'rcstyle-dim') {
                if (enable) {
                    element.classList.add('s-dim');
                } else {
                    element.classList.remove('s-dim');
                }
            }
        });
    }

    function changeColor(rcElementType) {
        const colorSelect = document.getElementById("color-select");

        const pyCodeInputs = document.querySelectorAll("span.rccfg-style-option.rcpycode");
        pyCodeInputs.forEach(pyCode => {
            pyCode.textContent = colorSelect.value.replace('c-', '');;
        });

        const elements = document.querySelectorAll('span.rc-element.'.concat(rcElementType));
        elements.forEach(element => {
            element.classList.forEach(classLabel => {
                if (classLabel.startsWith('c-')) {
                    element.classList.remove(classLabel)
                }
            });
            if (colorSelect.value !== '') {
                element.classList.add(colorSelect.value);
            }
        });
    }
</script>

<pre><code>import rich_click as click

click.rich_click.STYLE_OPTION = "<span class="rccfg-style-option rcpycode"></span>"
</code></pre>

<pre><code> Usage: docs.py [OPTIONS] FOO COMMAND [ARGS]...                                  
                                                                                 
 Help text for CLI                                                               
                                                                                 
╭─ Options ─────────────────────────────────────────────────────────────────────╮
│ <span class="rc-element rccfg-style-option">--bar</span>     INTEGER  Lorem ipsum [default: (someval)]                           │
│ <span class="rc-element rccfg-style-option">--help</span>             Show this message and exit.                                │
╰───────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────╮
│ subcommand               Help text for subcommand                             │
│ subgroup                 Help text for subgroup                               │
╰───────────────────────────────────────────────────────────────────────────────╯
</code></pre>
