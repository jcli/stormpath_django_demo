var addEvent = (function () {
    if (document.addEventListener) {
        return function (el, type, fn) {
            if (el && el.nodeName || el === window) {
                el.addEventListener(type, fn, false);
            } else if (el && el.length) {
                for (var i = 0; i < el.length; i++) {
                    addEvent(el[i], type, fn);
                }
            }
        };
    } else {
        return function (el, type, fn) {
            if (el && el.nodeName || el === window) {
                el.attachEvent('on' + type, function () { return fn.call(el, window.event); });
            } else if (el && el.length) {
                for (var i = 0; i < el.length; i++) {
                    addEvent(el[i], type, fn);
                }
            }
        };
    }
})();


addEvent(window, 'load', function() {
    var drop          = document.getElementById('drop');
    
    function cancel(e) {
        if (e.preventDefault) e.preventDefault();
        return false;
    }
    
    //Tells the browser that we can drop on this target
    addEvent(drop, 'dragover', cancel);  //DOM event
    addEvent(drop, 'dragenter', cancel); //IE event
	
    addEvent(drop, 'drop', function (e) {
        if (e.preventDefault) e.preventDefault(); // stops the browser from redirecting off to the text.
        console.log('got a item')
        console.log(e)
        console.log(drop)
        console.log(e.dataTransfer.getData('Text'))
		return false;
    });
});

