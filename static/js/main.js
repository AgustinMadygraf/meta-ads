/*
Path: static/js/main.js
*/

document.getElementById('adAccountForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const accountId = document.getElementById('account_id').value;
    const res = await fetch(`/ad_account/${accountId}`);
    const data = await res.json();
    document.getElementById('result').textContent = JSON.stringify(data, null, 2);
});
