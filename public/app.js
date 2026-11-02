(function(){
  var cards=[].slice.call(document.querySelectorAll('#grid .card'));
  var q=document.getElementById('q'),cnt=document.getElementById('count'),empty=document.getElementById('empty');
  var chips=[].slice.call(document.querySelectorAll('.chip'));
  var f='all';
  function norm(s){return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');}
  function run(){
    var t=norm(q.value.trim()),n=0;
    cards.forEach(function(c){
      var ok=(f==='all'||c.dataset.p===f)&&(!t||norm(c.dataset.q).indexOf(t)>-1);
      c.hidden=!ok;if(ok)n++;
    });
    cnt.textContent=n+' materi';empty.hidden=n>0;
  }
  function setF(v,scroll){
    f=v;chips.forEach(function(c){c.classList.toggle('on',c.dataset.f===v);});run();
    try{var u=new URL(location.href);if(v==='all')u.searchParams.delete('p');else u.searchParams.set('p',v);history.replaceState(null,'',u);}catch(e){}
    if(scroll)document.getElementById('materi').scrollIntoView({behavior:'smooth'});
  }
  chips.forEach(function(c){c.addEventListener('click',function(){setF(c.dataset.f);});});
  [].slice.call(document.querySelectorAll('.pil')).forEach(function(p){p.addEventListener('click',function(){setF(p.dataset.f,true);});});
  q.addEventListener('input',run);
  var p=new URLSearchParams(location.search).get('p');
  setF(p&&/^P[0-5]$/.test(p)?p:'all');
})();
