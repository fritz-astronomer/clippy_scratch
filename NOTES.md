# Vue!!!

https://router.vuejs.org/guide/
https://pinia.vuejs.org/
https://vuetifyjs.com/en/components/navigation-drawers/

https://github.com/jvns/vue3-tiny-template/blob/main/index.html


# ULKit - seems to work well
https://getuikit.com/docs/navbar
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/uikit@3.15.24/dist/css/uikit.min.css" />
<script src="https://cdn.jsdelivr.net/npm/uikit@3.15.24/dist/js/uikit.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/uikit@3.15.24/dist/js/uikit-icons.min.js"></script>

<!--umbrella, jquerylike -->
<!--https://umbrellajs.com/documentation-->
<script src="https://cdn.jsdelivr.net/npm/umbrellajs@3.3.1/umbrella.min.js"></script>

<script>
UIkit.util.ready(function() {
    UIkit.offcanvas('#panel').show();
    u("header div.navbar").attr({ style: 'z-index: 1' });
});
</script>


<!-- This is a button toggling the off-canvas -->
<!--<button uk-toggle="target: #my-id" type="button">####</button>-->

<!-- This is an anchor toggling the off-canvas -->
<!--<a href="#my-id" uk-toggle>###</a>-->

<!-- This is the off-canvas -->
<div id="clippy" class="uk-animation-fade uk-animation-reverse"></div>
<div id="panel" uk-offcanvas="flip: true; mode: push; container: body">
    <div class="uk-offcanvas-bar">
        <button class="uk-offcanvas-close" type="button" uk-close></button>
    </div>
</div>
```

# Petite Vue?
```html
<script type="module">
  import { createApp } from 'https://unpkg.com/petite-vue?module'

  createApp({
    // exposed to all expressions
    count: 0,
    // getters
    get plusOne() {
      return this.count + 1
    },
    // methods
    increment() {
      this.count++
    }
  }).mount()
</script>

<!-- v-scope value can be omitted -->
<div v-scope>
  <p>{{ count }}</p>
  <p>{{ plusOne }}</p>
  <button @click="increment">increment</button>
</div>
```

# Semantic UI - worked well
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.5.0/dist/semantic.min.css">
<script
  src="https://code.jquery.com/jquery-3.1.1.min.js"
  integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
  crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.5.0/dist/semantic.min.js"></script>
<script>
$('div.container').classList.add("pusher")
$('.ui.sidebar').sidebar('visible');
</script>

<style>
    #clippy {
        padding-top: 100px;
    }
</style>

<div id="clippy" class="ui sidebar visible inverted vertical menu">
    <a class="item">
        1
    </a>
    <a class="item">
        2
    </a>
    <a class="item">
        3
    </a>
</div>
```

# Foundation, haven't tried
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/foundation-sites@6.7.5/dist/css/foundation.min.css" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/foundation-sites@6.7.5/dist/js/foundation.min.js" crossorigin="anonymous"></script>
```

# cash - jquerylike
https://github.com/fabiospampinato/cash


# Bootstrap - messed up existing nav

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasScrolling" aria-controls="offcanvasScrolling">Enable body scrolling</button>
<div class="offcanvas offcanvas-start" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1" id="offcanvasScrolling" aria-labelledby="offcanvasScrollingLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasScrollingLabel">Offcanvas with body scrolling</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <p>Try scrolling the rest of the page to see this option in action.</p>
  </div>
</div>
```

# Alpine, worked fine, didn't do much
```html
<script src="//unpkg.com/alpinejs" defer></script>
<div x-data="{ open: false }">
    <button @click="open = true">Expand</button>

    <span x-show="open">
      Content...
    </span>
</div>
```