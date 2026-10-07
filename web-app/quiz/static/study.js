const form = document.querySelector('#quiz-form');
const status = document.querySelector('#save-status');
const timer = document.querySelector('#timer');
const end = Date.now() + Number(timer.dataset.seconds) * 1000;
let chain = Promise.resolve();
let submitting = false;
form.addEventListener('change', () => {
  document.querySelector('#progress').textContent = form.querySelectorAll('input[type=radio]:checked').length;
  const body = new FormData(form);
  status.textContent = 'Salvando…';
  chain = chain.then(async () => {
    try {
      const response = await fetch(location.href, {method: 'POST', body, headers: {'X-Autosave':'1'}});
      if (!response.ok) throw new Error('save');
      const result = await response.json();
      status.textContent = 'Respostas salvas';
      if (result.finished) location.reload();
    } catch (_) {
      status.textContent = 'Falha ao salvar. Use “Salvar respostas” para tentar novamente.';
    }
  });
});
form.addEventListener('submit', (event) => {
  if (event.submitter?.value === 'finish' && !confirm('Finalizar a rodada? As respostas não poderão ser alteradas.')) event.preventDefault();
  else submitting = true;
});
setInterval(() => {
  const remaining = Math.max(0, Math.ceil((end-Date.now())/1000));
  timer.textContent = `${String(Math.floor(remaining/60)).padStart(2,'0')}:${String(remaining%60).padStart(2,'0')}`;
  if (!remaining && !submitting) {submitting = true; location.reload();}
}, 250);
