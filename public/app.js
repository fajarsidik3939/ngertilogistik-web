(function(){
  // daftar artikel: cari + filter kategori
  var grid=document.getElementById('grid');
  if(grid){
    var cards=[].slice.call(grid.querySelectorAll('.post'));
    var q=document.getElementById('q'),cnt=document.getElementById('count'),empty=document.getElementById('empty');
    var chips=[].slice.call(document.querySelectorAll('.chip')),f='all';
    var norm=function(s){return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');};
    var run=function(){var t=norm(q.value.trim()),n=0;
      cards.forEach(function(c){var ok=(f==='all'||c.dataset.k===f)&&(!t||norm(c.dataset.q).indexOf(t)>-1);c.hidden=!ok;if(ok)n++;});
      cnt.textContent=n+' artikel';empty.hidden=n>0;};
    chips.forEach(function(c){c.addEventListener('click',function(){f=c.dataset.f;chips.forEach(function(x){x.classList.toggle('on',x===c);});run();});});
    q.addEventListener('input',run);
    var p=new URLSearchParams(location.search);if(p.get('q'))q.value=p.get('q');
    run();
  }
  // daftar isi: tandai bagian yang sedang dibaca
  var links=[].slice.call(document.querySelectorAll('.toc a'));
  if(links.length&&'IntersectionObserver' in window){
    var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(a){a.classList.remove('on');});var a=map[e.target.id];if(a)a.classList.add('on');}});},{rootMargin:'-80px 0px -70% 0px'});
    Object.keys(map).forEach(function(id){var h=document.getElementById(id);if(h)io.observe(h);});
  }
})();
