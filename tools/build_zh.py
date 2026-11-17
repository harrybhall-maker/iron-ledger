"""Build the Chinese beginner-programme copy of Iron Ledger into <repo>/zh/."""
import re, sys, pathlib, shutil
repo = pathlib.Path(sys.argv[1]); VERSION = sys.argv[2]
out = repo / 'zh'
h = (repo / 'index.html').read_text(encoding='utf-8')

def rep(old, new, count=1):
    global h
    n = h.count(old)
    if count == 'all':
        if n == 0: raise SystemExit(f'not found: {old[:80]!r}')
    elif n != count:
        raise SystemExit(f'expected {count} match(es), found {n}: {old[:80]!r}')
    h = h.replace(old, new)

def resub(pat, new, count=1):
    global h
    h2, n = re.subn(pat, new, h, count=0 if count == 'all' else count, flags=re.S)
    if n == 0: raise SystemExit('regex not found: ' + pat[:80])
    h = h2

# ================= separate storage, cache and identity =================
rep("const LSKEY = 'ironledger.v1';", "const LSKEY = 'ironledger.zh.v1';")
rep("const TABKEY = 'ironledger.tab';", "const TABKEY = 'ironledger.zh.tab';")
rep('<html lang="en">', '<html lang="zh-CN">')
resub(r'<title>.*?</title>', '<title>训练记录</title>')
rep('<meta name="apple-mobile-web-app-title" content="Iron Ledger">', '<meta name="apple-mobile-web-app-title" content="训练记录">')

# ================= the programme =================
PROGRAM_ZH = r"""const PROGRAM = {
  intro: { label:'入门课', items:[] },
  a: { label:'训练A', items:[
    { k:'goblet', n:'高脚杯深蹲', m:'股四头肌', t:'10–15', vars:[
      { id:'db', n:'哑铃高脚杯深蹲', w:8, u:'kg' }, { id:'heels', n:'垫脚跟哑铃深蹲', w:6, u:'kg/只' },
      { id:'smith', n:'史密斯深蹲', w:10, u:'kg' }, { id:'hack', n:'哈克深蹲', w:10, u:'kg' },
      { id:'legpress', n:'腿举', w:30, u:'kg' }, { id:'bb', n:'杠铃深蹲', w:20, u:'kg' } ] },
    { k:'hipthrust', n:'臀推', m:'臀', t:'10–15', vars:[
      { id:'bb', n:'杠铃臀推', w:20, u:'kg' }, { id:'mach', n:'臀推机', w:20, u:'kg' },
      { id:'smith', n:'史密斯臀推', w:20, u:'kg' }, { id:'bridge', n:'哑铃臀桥', w:10, u:'kg' },
      { id:'single', n:'单腿哑铃臀推', w:0, u:'kg', bw:true } ] },
    { k:'pulldown', n:'高位下拉', m:'背阔肌', t:'10–15', vars:[
      { id:'wide', n:'宽握下拉', w:20, u:'kg' }, { id:'neutral', n:'对握下拉', w:20, u:'kg' },
      { id:'single', n:'单臂绳索下拉', w:7.5, u:'kg/侧' } ] },
    { k:'latraise', n:'侧平举', m:'肩中束', t:'10–15', vars:[
      { id:'db', n:'哑铃侧平举', w:2, u:'kg/只' }, { id:'cable', n:'绳索侧平举', w:2.5, u:'kg/侧' },
      { id:'mach', n:'侧平举机', w:10, u:'kg' }, { id:'seated', n:'坐姿哑铃侧平举', w:2, u:'kg/只' } ] },
    { k:'reardelt', n:'反向飞鸟 / 面拉', m:'肩后束', t:'10–15', vars:[
      { id:'pec', n:'反向蝴蝶机', w:10, u:'kg' }, { id:'face', n:'绳索面拉', w:10, u:'kg' },
      { id:'db', n:'俯身哑铃反向飞鸟', w:2, u:'kg/只' }, { id:'cable', n:'绳索反向飞鸟', w:2.5, u:'kg/侧' },
      { id:'band', n:'弹力带拉开', w:0, u:'kg', bw:true } ] },
  ]},
  b: { label:'训练B', items:[
    { k:'rdl', n:'罗马尼亚硬拉', m:'腘绳肌', t:'10–15', vars:[
      { id:'db', n:'哑铃罗马尼亚硬拉', w:8, u:'kg/只' }, { id:'bb', n:'杠铃罗马尼亚硬拉', w:20, u:'kg' },
      { id:'single', n:'单腿哑铃罗马尼亚硬拉', w:6, u:'kg' }, { id:'ext', n:'45°背伸', w:0, u:'kg', bw:true },
      { id:'pull', n:'绳索后拉', w:10, u:'kg' } ] },
    { k:'bss', n:'保加利亚分腿蹲（身体前倾）', m:'臀', t:'10–15', vars:[
      { id:'db', n:'哑铃分腿蹲', w:4, u:'kg/只' }, { id:'rlunge', n:'后撤弓步', w:4, u:'kg/只' },
      { id:'wlunge', n:'行走弓步', w:4, u:'kg/只' }, { id:'step', n:'高台阶上步', w:4, u:'kg/只' },
      { id:'smith', n:'史密斯分腿蹲', w:10, u:'kg' } ] },
    { k:'row', n:'坐姿绳索划船', m:'上背', t:'10–15', vars:[
      { id:'cable', n:'坐姿绳索划船', w:20, u:'kg' }, { id:'chest', n:'胸部支撑哑铃划船', w:6, u:'kg/只' },
      { id:'single', n:'单臂哑铃划船', w:8, u:'kg' }, { id:'mach', n:'器械划船', w:20, u:'kg' },
      { id:'inv', n:'反向划船', w:0, u:'kg', bw:true } ] },
    { k:'incline', n:'上斜哑铃卧推', m:'胸', t:'10–15', vars:[
      { id:'db', n:'上斜哑铃卧推', w:5, u:'kg/只' }, { id:'flat', n:'平板哑铃卧推', w:5, u:'kg/只' },
      { id:'mach', n:'上斜器械推胸', w:10, u:'kg' }, { id:'smith', n:'史密斯上斜卧推', w:10, u:'kg' },
      { id:'cable', n:'绳索推胸', w:5, u:'kg/侧' }, { id:'pushup', n:'俯卧撑', w:0, u:'kg', bw:true } ] },
    { k:'abduction', n:'髋外展', m:'臀', t:'10–15', vars:[
      { id:'mach', n:'髋外展机', w:20, u:'kg' }, { id:'cable', n:'绳索站姿外展', w:2.5, u:'kg' },
      { id:'walk', n:'弹力带侧向走', w:0, u:'kg', bw:true }, { id:'seated', n:'坐姿弹力带外展', w:0, u:'kg', bw:true } ] },
  ]},
};

/* ---------- Her programme timeline ---------- */
const START = '2026-11-30';       // week 1 starts Monday 30 Nov; the intro session comes before it
function progWeek(iso){
  if (iso < START) return 0;
  return Math.floor((new Date(weekStart(iso)+'T12:00:00') - new Date(START+'T12:00:00')) / 604800000) + 1;
}
function phaseOf(iso){
  const w = progWeek(iso);
  if (w <= 0) return { w:w, s:1, key:'intro' };
  if (w === 1) return { w:w, s:2, key:'easy' };
  if (w <= 3) return { w:w, s:3, key:'hard' };
  return { w:w, s:3, key:'fail' };
}
function wkLabel(iso){ const w = progWeek(iso); return w >= 1 ? '第'+w+'周' : (w === 0 ? '入门' : '更早'); }
const RULES = '第一组的目标是10–15次。之后几组次数下降没关系，但如果某组只有5次或更少，下一组就要减重。任何一组超过15次，下周加重。';
function phaseNote(iso){
  const p = phaseOf(iso);
  if (p.key === 'intro') return '<b>入门课</b>：每个动作先做2–3组轻重量热身，专心学动作。然后做<b>1组正式组</b>，下放时慢数3–4秒，'
    + '做到10–15次、还能再做2–3次时停下。目的是学会动作，接下来几天肌肉会酸痛，这是正常的，不要做得太累。';
  if (p.key === 'easy') return '<b>第1周</b>：每个动作<b>2组</b>正式组，每组结束时还能再做2–3次。' + RULES;
  if (p.key === 'hard') return '<b>第'+p.w+'周</b>：每个动作<b>3组</b>，要比较吃力，每组结束时只能再做1–2次。' + RULES;
  return '<b>第'+p.w+'周</b>：每个动作<b>3组</b>，接近力竭：做到再多一次就很难保持动作标准为止。' + RULES;
}
/* planned sets follow the calendar, not a fixed number */
Object.keys(PROGRAM).forEach(function(d){
  PROGRAM[d].items.forEach(function(it){
    Object.defineProperty(it, 's', { enumerable:true, get:function(){ return phaseOf(todayKey()).s; } });
  });
});
function incW(w){ return w < 10 ? 1 : 2.5; }
function lowerW(w){
  if (w == null || w <= 0) return w;
  const step = w < 10 ? 1 : 2.5;
  return Math.max(step, Math.round((w * 0.8) / step) * step);
}
"""
resub(r"const PROGRAM = \{.*?\n\};\n", PROGRAM_ZH.replace('\\', '\\\\'))

rep("""const MUSCLES = ['Chest','Side delts','Rear delts','Triceps','Biceps','Lats','Upper back',
                 'Traps','Forearms','Quads','Glutes','Hamstrings','Calves','Abs','Lower back'];""",
    """const MUSCLES = ['胸','肩中束','肩后束','肱三头肌','肱二头肌','背阔肌','上背',
                 '斜方肌','前臂','股四头肌','臀','腘绳肌','小腿','腹部','下背'];""")
rep("'Other'", "'其他'", 'all')
rep('<option value="Other">Other</option>', '<option value="其他">其他</option>')

# ---------- days: intro + A (Mon/Tue) + B (Wed/Thu) ----------
rep("const BUILTIN = ['push','pull','legs','smalls'];", "const BUILTIN = Object.keys(PROGRAM);")
rep("const WDN = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];", "const WDN = ['周日','周一','周二','周三','周四','周五','周六'];")
rep("""  return [ { id:'push', label:'Push', wd:1, c:0 }, { id:'pull', label:'Pull', wd:2, c:1 },
           { id:'legs', label:'Legs', wd:3, c:2 }, { id:'smalls', label:'Smalls', wd:5, c:3 } ];""",
    """  return [ { id:'intro', label:'入门课', wd:null, c:2 },
           { id:'a', label:'训练A', wd:1, wd2:2, c:5 }, { id:'b', label:'训练B', wd:3, wd2:4, c:1 } ];""")
rep("order:{push:[],pull:[],legs:[],smalls:[]}, days: defaultDays() };", "order:{intro:[],a:[],b:[]}, days: defaultDays() };")
rep("""    if (!(typeof d.wd === 'number' && d.wd >= 0 && d.wd <= 6)) d.wd = null;""",
    """    if (!(typeof d.wd === 'number' && d.wd >= 0 && d.wd <= 6)) d.wd = null;
    if (!(typeof d.wd2 === 'number' && d.wd2 >= 0 && d.wd2 <= 6)) d.wd2 = null;""")
rep("""function dayLabel(id){""", """function wdText(d){
  if (d.wd == null) return '&nbsp;';
  return WDN[d.wd] + (d.wd2 != null ? '/' + WDN[d.wd2].slice(1) : '');
}
function dayLabel(id){""")
rep("""        + '<span class="wd">'+(d.wd == null ? '&nbsp;' : WDN[d.wd])+'</span></button>';""",
    """        + '<span class="wd">'+wdText(d)+'</span></button>';""")
rep("""    } else d.wd = ev.target.value === '' ? null : parseInt(ev.target.value, 10);""",
    """    } else { d.wd = ev.target.value === '' ? null : parseInt(ev.target.value, 10); d.wd2 = null; }""")
rep("""  const byDay = state.days.filter(function(d){ return !d.gone && d.wd === today; })[0];""",
    """  if (todayKey() < START && dayObj('intro') && !dayObj('intro').gone) return 'intro';
  const byDay = state.days.filter(function(d){ return !d.gone && (d.wd === today || d.wd2 === today); })[0];""")
# the intro session shows every exercise from the other days
rep("""function dayItems(day){
  return orderItems(day, everyItem().filter(function(it){""",
    """function dayItems(day){
  if (day === 'intro'){
    let all = [];
    DAYS.forEach(function(d){ if (d !== 'intro') all = all.concat(dayItems(d)); });
    return all;
  }
  return orderItems(day, everyItem().filter(function(it){""")
rep("""  DAYS.forEach(function(d){
    dayItems(d).forEach(function(it){ out[it.m] = (out[it.m] || 0) + (it.s || 0); });""",
    """  DAYS.forEach(function(d){
    if (d === 'intro') return;
    dayItems(d).forEach(function(it){ out[it.m] = (out[it.m] || 0) + (it.s || 0); });""")
# after the intro week the intro tab tidies itself away (history kept, restorable)
rep("""  syncDays(); renderTabs();
  tab = initialTab();""",
    """  const intro = dayObj('intro');
  if (intro && todayKey() >= START && !intro.retired){ intro.gone = true; intro.retired = true; markMeta(); }
  syncDays(); renderTabs();
  tab = initialTab();""")

# ---------- weeks are programme weeks ----------
resub(r"function weekNo\(iso\)\{.*?\n\}\n", "function weekNo(iso){ return progWeek(iso); }\n")

# ---------- prefill: sets follow the phase; >15 reps last time means heavier ----------
rep("""function prefillRows(item, variant){
  const prev = prevEntry(item.k, todayKey(), variant.id);
  if (prev) return prev.sets.map(function(s){ return s.k ? { w:s.w, r:null, k:s.k } : { w:s.w, r:null }; });
  const rows = [];
  for (let i=0;i<item.s;i++) rows.push({ w: variant.w, r:null });
  return rows;
}""",
"""function progressFrom(prev){
  const straight = prev.sets.filter(function(s){ return !s.k && s.r != null; });
  if (!straight.length) return null;
  const w0 = straight[0].w;
  const up = straight.some(function(s){ return s.r > 15; });
  return { w0:w0, up:up, w: (up && w0 != null) ? Math.round((w0 + incW(w0)) * 100) / 100 : w0 };
}
function prefillRows(item, variant){
  const prev = prevEntry(item.k, todayKey(), variant.id);
  const pr = prev ? progressFrom(prev) : null;
  const w = pr ? pr.w : variant.w;
  const rows = [];
  for (let i=0;i<item.s;i++) rows.push({ w: w, r:null });
  return rows;
}""")

# ---------- card hints (Chinese + rule reminders) ----------
rep("""  if (prev){
    hint = 'Last (Wk'+weekNo(prev.date)+' · '+fmtDate(prev.date)+'): <b>'+esc(fmtSets(prev.sets, variant))+'</b>';
  } else {
    const sw = variant.bw && variant.w === 0 ? 'bodyweight' : variant.w + ' ' + variant.u;
    hint = 'Suggested start: <b>'+esc(sw)+'</b> — calibrate, leave 2–3 in the tank';
  }""",
"""  if (prev){
    hint = '上次（'+wkLabel(prev.date)+' · '+fmtDate(prev.date)+'）：<b>'+esc(fmtSets(prev.sets, variant))+'</b>';
    const pr = progressFrom(prev);
    if (pr && pr.up && !variant.bw) hint += '<br><span class="upnote">上次有一组超过15次 → 今天加重到 '+esc(fmtW(pr.w, variant))+' '+esc(variant.u)+'</span>';
    else if (pr && pr.up) hint += '<br><span class="upnote">上次有一组超过15次 → 今天加点负重或换更难的动作</span>';
  } else {
    const sw = variant.bw && variant.w === 0 ? '自重' : variant.w + ' ' + variant.u;
    hint = '建议起始重量：<b>'+esc(sw)+'</b>（只是参考）— 选一个第一组能做10–15次的重量';
  }
  (st.sets || []).forEach(function(s, i){
    if (s.k || s.r == null) return;
    if (s.r <= 5 && i < st.sets.length - 1) hint += '<br><span class="lownote">第'+(i+1)+'组只做了'+s.r+'次 → 下一组减重（已自动降低约20%）</span>';
    if (s.r > 15) hint += '<br><span class="upnote">第'+(i+1)+'组超过15次 → 下周加重</span>';
  });""")
rep("  .myochip { margin-left: auto; }",
    "  .myochip { margin-left: auto; }\n  .lownote { color: var(--bad); font-weight: 600; }\n  .upnote { color: var(--pull); font-weight: 600; }")

# ≤5 reps: lower the weight of the sets still to do
rep("""document.getElementById('view').addEventListener('change', function(ev){""",
    """document.getElementById('view').addEventListener('change', function(ev){
  if (ev.target.classList.contains('rin')){
    const card = ev.target.closest('.card'), row = ev.target.closest('.set');
    if (!card || !row || DAYS.indexOf(tab) < 0) return;
    const r = parseR(ev.target.value);
    if (r == null || r > 5 || row.dataset.kind) return;
    commitCard(card);
    const item = itemByKey(card.dataset.k); if (!item) return;
    const st = curSession(tab).ex[item.k]; if (!st) return;
    const i = parseInt(row.dataset.i, 10), w = st.sets[i] && st.sets[i].w;
    let changed = false;
    for (let j=i+1;j<st.sets.length;j++){
      const s = st.sets[j];
      if (s.r == null && !s.k && s.w != null && w != null && s.w >= w){ s.w = lowerW(w); changed = true; }
    }
    if (changed){ curSession(tab).u = Date.now(); dirty = true; persistLocal(); renderDay(tab); refreshPill(); toast('只有'+r+'次 — 后面几组已减重'); }
    return;
  }""")

# day page: phase note, no list-editing / adding on the intro day
rep("""    : '<div class="rirnote">Work near the top of each target range with 2–3 reps left in the tank; hit the range’s ceiling on every set, then add weight next time.</div>';""",
    """    : '<div class="rirnote">'+phaseNote(todayKey())+(day === 'intro' ? '' : '<br><span class="hold">动作还没定的话，点动作下面的选项换成别的器械或动作。</span>')+'</div>';""")
rep("""    + '<button type="button" class="editbtn'+(editing?' on':'')+'" data-act="edittoggle">'+(editing?'Done':'Edit list')+'</button></span></div>';""",
    """    + (day === 'intro' ? '' : '<button type="button" class="editbtn'+(editing?' on':'')+'" data-act="edittoggle">'+(editing?'完成':'编辑动作')+'</button>')+'</span></div>';""")
rep("""  html += adding ? addFormHTML(day)
                 : '<button type="button" class="addex" data-act="addopen">+ Add exercise to '+esc(dayLabel(day))+'</button>';""",
    """  if (day !== 'intro') html += adding ? addFormHTML(day)
                 : '<button type="button" class="addex" data-act="addopen">+ 给'+esc(dayLabel(day))+'添加动作</button>';""")
rep("""  let html = '<div class="dayline"><span class="d">'+esc(dayLabel(day))+' Day</span>'
    + '<span class="rt"><span class="wk mono">Wk '+weekNo(todayKey())+' · '+fmtDate(todayKey())+'</span>'
    + '<span class="wk mono">'+planned+' sets planned</span>'""",
    """  let html = '<div class="dayline"><span class="d">'+esc(dayLabel(day))+'</span>'
    + '<span class="rt"><span class="wk mono">'+wkLabel(todayKey())+' · '+fmtDate(todayKey())+'</span>'
    + '<span class="wk mono">计划 '+planned+' 组</span>'""")

# ================= translation =================
T = [
 ('>Iron Ledger<', '>训练记录<'),
 ('<button data-tab="weeks">Weeks</button>', '<button data-tab="weeks">每周</button>'),
 ('<button data-tab="hist">History</button>', '<button data-tab="hist">历史</button>'),
 ('<button data-tab="days">Days</button>', '<button data-tab="days">训练日</button>'),
 ('Save session', '保存'),
 ("toLocaleDateString('en-GB', { weekday:'short', day:'numeric', month:'short' })", "toLocaleDateString('zh-CN', { month:'long', day:'numeric', weekday:'short' })"),
 ("toLocaleDateString('en-GB', { day:'numeric', month:'short' })", "toLocaleDateString('zh-CN', { month:'long', day:'numeric' })"),
 ("'en-GB'", "'zh-CN'"),
 ("const nm = kind === 'm' ? 'myo mini-set' : kind === 'd' ? 'drop set' : 'normal set';", "const nm = kind === 'm' ? '休息暂停小组' : kind === 'd' ? '递减组' : '普通组';"),
 (", tap to change type\">", "，点一下切换类型\">"),
 ('aria-label="less weight"', 'aria-label="减重量"'), ('aria-label="more weight"', 'aria-label="加重量"'),
 ('aria-label="fewer reps"', 'aria-label="减次数"'), ('aria-label="more reps"', 'aria-label="加次数"'),
 ('aria-label="remove set"', 'aria-label="删除这组"'), ('aria-label="move up"', 'aria-label="上移"'),
 ('aria-label="move down"', 'aria-label="下移"'),
 ('data-act="rmex">Remove</button>', 'data-act="rmex">移除</button>'),
 ('<span class="lbl">Day</span>', '<span class="lbl">训练日</span>'),
 ('data-act="myomode">Myo-reps</button>', 'data-act="myomode">休息暂停法</button>'),
 ('tap # → <b>m</b> myo · <i>↘</i> drop', '点序号 → <b>m</b> 暂停组 · <i>↘</i> 递减组'),
 ("<span>weight (", "<span>重量 ("), (")</span><span>reps</span>", ")</span><span>次数</span>"),
 ('Marked not done for today — tap below to undo.', '今天标记为没做 — 点下面的按钮可撤销。'),
 ('<span class="target">target <b>', '<span class="target">目标 <b>'),
 ('data-act="addset">+ set</button>', 'data-act="addset">+ 组</button>'),
 ('data-act="addmyo">+ myo</button>', 'data-act="addmyo">+ 暂停组</button>'),
 ('data-act="adddrop">+ drop</button>', 'data-act="adddrop">+ 递减组</button>'),
 ("'Not done ✓'", "'没做 ✓'"), ("'Not done'", "'没做'"),
 ('<h4>New exercise · ', '<h4>新动作 · '),
 ('<label for="nf_n">Exercise name</label>', '<label for="nf_n">动作名称</label>'),
 ('placeholder="e.g. Machine Chest Press"', 'placeholder="例如：器械推胸"'),
 ('Muscle group (for weekly totals)', '肌群（用于每周统计）'),
 ('<label for="nf_t">Target reps</label>', '<label for="nf_t">目标次数</label>'),
 ('<label for="nf_s">Sets</label>', '<label for="nf_s">组数</label>'),
 ('<label for="nf_w">Start weight</label>', '<label for="nf_w">起始重量</label>'),
 ('<label for="nf_u">Unit label</label>', '<label for="nf_u">单位</label>'),
 ('Bodyweight move — weight means <em>added</em> load', '自重动作 — 重量指<em>额外</em>负重'),
 ('data-act="addcancel">Cancel</button>', 'data-act="addcancel">取消</button>'),
 ('data-act="addsubmit">Add exercise</button>', 'data-act="addsubmit">添加动作</button>'),
 ('<div class="rmhead">Removed from ', '<div class="rmhead">已从此训练日移除：'),
 ('">Restore</button>', '">恢复</button>'),
 ('data-act="purge" data-rk="\'+esc(it.k)+\'">Delete</button>', 'data-act="purge" data-rk="\'+esc(it.k)+\'">删除</button>'),
 ('Reorder with ↑↓, move an exercise to another day with the Day chips, or Remove it from this day. <b>Remove</b> keeps the history and can be undone; <b>Delete</b> (in the removed list) wipes the exercise and its logged sets for good.',
  '用 ↑↓ 调整顺序，用“训练日”按钮把动作移到另一天，或把它从这一天移除。<b>移除</b>会保留记录，可以撤销；<b>删除</b>（在已移除列表里）会永久删掉这个动作和它的记录。'),
 ('<p class="hnone">No exercises on this day yet — add one below.</p>', '<p class="hnone">这一天还没有动作 — 在下面添加。</p>'),
 ('aria-label="previous week"', 'aria-label="上一周"'), ('aria-label="next week"', 'aria-label="下一周"'),
 ("(wn >= 1 ? 'Week '+wn : 'Earlier')", "(wn >= 1 ? '第'+wn+'周' : (wn === 0 ? '入门周' : '更早'))"),
 ('<span>Sets by muscle group</span>', '<span>各肌群组数</span>'),
 ('<p class="vnone">Nothing planned or logged yet.</p>', '<p class="vnone">还没有计划或记录。</p>'),
 ('Myo mini-sets count as ⅔ of a set, drop sets as ½.', '暂停小组按⅔组计算，递减组按½组计算。'),
 ('<p class="hnone">No sessions logged this week.</p>', '<p class="hnone">这周还没有训练记录。</p>'),
 ('<span class="hskip">not done</span>', '<span class="hskip">没做</span>'),
 ("'<span class=\"hdate\">Wk'+weekNo(sess.date)+' · '", "'<span class=\"hdate\">'+wkLabel(sess.date)+' · '"),
 ('">clear</button>', '">清除</button>'),
 ('<em>removed</em>', '<em>已移除</em>'),
 ("'<p class=\"hnone\">Nothing logged for '+esc(dayLabel(day))+' yet — your first saved session lands here.</p>'",
  "'<p class=\"hnone\">'+esc(dayLabel(day))+'还没有记录 — 保存第一次训练后会显示在这里。</p>'"),
 ('<summary>Backup &amp; restore</summary>', '<summary>备份与恢复</summary>'),
 ('Copy this somewhere safe (Notes, an email to yourself) — it is your whole log as text, and can be pasted back in below.',
  '把这段文字复制保存到安全的地方（备忘录、微信发给自己等）— 这是你全部的训练记录，可以在下面粘贴回来恢复。'),
 ('data-act="bkcopy">Copy backup</button>', 'data-act="bkcopy">复制备份</button>'),
 ('data-act="bkfile">Save backup file</button>', 'data-act="bkfile">保存备份文件</button>'),
 ('placeholder="Paste a backup here…"', 'placeholder="在这里粘贴备份…"'),
 ('data-act="bkimport">Import (replaces everything)</button>', 'data-act="bkimport">导入（会覆盖全部记录）</button>'),
 ('>Load backup file<input', '>读取备份文件<input'),
 ('<summary>Where your data is stored</summary>', '<summary>数据保存在哪里</summary>'),
 ('Your log is stored on this phone only, inside the Home Screen app, and works with no signal. It does not sync to other devices. Every so often, use Save backup file above and keep the file in Files or iCloud Drive. If you delete the Home Screen icon, the log goes with it.',
  '训练记录只保存在这部手机上（主屏幕上的这个应用里），没有网络也能用，不会同步到其他设备。请时不时用上面的“保存备份文件”，把文件存到“文件”或 iCloud 云盘。如果删除主屏幕图标，记录也会一起删除。'),
 ('>App version ', '>版本 '),
 ("(b?'yes':'no')", "(b?'是':'否')"),
 ("'<div>Works offline: '", "'<div>离线可用：'"),
 ("'still setting up — open once with signal'", "'还在准备中 — 请在有网络时打开一次'"),
 ("'not supported in this browser'", "'这个浏览器不支持'"),
 ("'<div>This phone’s storage: '", "'<div>手机存储：'"),
 ("'blocked — open the link directly in Safari'", "'被阻止 — 请直接在 Safari 中打开链接'"),
 ("'<div>Last saved: '", "'<div>上次保存：'"),
 ('<span class="no">never</span>', '<span class="no">从未</span>'),
 ("'<div>Last error: <span class=\"no\">'", "'<div>上次错误：<span class=\"no\">'"),
 ('aria-label="weekday"><option value="">No day</option>', 'aria-label="星期"><option value="">不固定</option>'),
 ('<div class="dhead">Workout days</div>', '<div class="dhead">训练日</div>'),
 ("Rename a day, set which weekday it opens on, reorder, or add and delete days. Tap the dot to change its colour. ",
  "可以改名、设置星期几自动打开、调整顺序，或添加和删除训练日。点圆点可以换颜色。"),
 ("'Deleting a day keeps its logged history and can be undone below. To keep an exercise, move it to another day first (Edit list › Day chips).</p>'",
  "'删除训练日会保留它的历史记录，也可以在下面恢复。想保留某个动作的话，先把它移到别的训练日（编辑动作 › 训练日）。</p>'"),
 ('aria-label="change colour"', 'aria-label="换颜色"'), ('aria-label="delete day"', 'aria-label="删除训练日"'),
 ("' exercise'+(n===1?'':'s')", "' 个动作'"),
 ('placeholder="New day name"', 'placeholder="新训练日名称"'),
 ('data-act="dadd">Add</button>', 'data-act="dadd">添加</button>'),
 ('<div class="rmhead">Deleted days</div>', '<div class="rmhead">已删除的训练日</div>'),
 ("pill.textContent = 'Unsaved'", "pill.textContent = '未保存'"),
 ("'Save' + (DAYS.indexOf(tab) >= 0 ? ' · ' + dayLabel(tab) : ' changes')", "'保存' + (DAYS.indexOf(tab) >= 0 ? ' · ' + dayLabel(tab) : '更改')"),
 ("state.savedAt ? 'Saved' : 'Ready'", "state.savedAt ? '已保存' : '就绪'"),
 ("pill.textContent = 'Not saving'", "pill.textContent = '无法保存'"),
 ("'<b>This browser is blocking storage.</b> Nothing you log here will be kept. '", "'<b>这个浏览器阻止了存储。</b>在这里记录的内容不会被保存。'"),
 ("'Open the app from your Home Screen icon (not a private tab), or copy a backup from History after each session.'", "'请从主屏幕图标打开应用（不要用无痕模式），或者每次训练后在“历史”里复制备份。'"),
 ("'<b>Moving from the old app?</b> In the old Iron Ledger, open History › Backup &amp; restore and tap Copy backup. '",
  "'<b>欢迎！</b>记录只保存在这部手机上，没网也能用。'"),
 ("'Then come back here, open History › Backup &amp; restore, paste it in and tap Import.'",
  "'先从“入门课”开始（11月22日周日）。'"),
 ("toast('Saved ✓')", "toast('已保存 ✓')"),
 ("'Can’t save here — copy a backup from History'", "'这里无法保存 — 请在“历史”里复制备份'"),
 ("btn.textContent = 'Saving…'", "btn.textContent = '保存中…'"),
 ("'Opened elsewhere — reloading to the newest copy'", "'在别处打开过 — 正在载入最新版本'"),
 ("'Saving too often — wait a minute, then Save again'", "'保存太频繁 — 请等一分钟再保存'"),
 ("'This view can’t save into the page — copy a backup from History'", "'这里无法保存 — 请在“历史”里复制备份'"),
 ("'Log too big to save — clear some old entries in History'", "'记录太大无法保存 — 请在“历史”里清除一些旧记录'"),
 ("'Save failed (' + c + ') — kept on this phone, try again'", "'保存失败（' + c + '）— 已保留在手机上，请再试一次'"),
 ("'Give the day a name'", "'请给训练日起个名字'"),
 ("'Added ' + nm + ' — open it to add exercises'", "'已添加' + nm + ' — 打开它来添加动作'"),
 ("btn.textContent = 'Delete?'", "btn.textContent = '删除？'"),
 ("' deleted — restore it below if needed'", "'已删除 — 需要的话可以在下面恢复'"),
 ("' restored'", "'已恢复'"),
 ("'Backup copied'", "'备份已复制'"),
 ("'Select the text and copy it manually'", "'请手动选中文字并复制'"),
 ("'Couldn’t make the file — use Copy backup instead'", "'无法生成文件 — 请改用“复制备份”'"),
 ("'Tap again to replace everything'", "'再点一次将覆盖全部记录'"),
 ("'Import (replaces everything)'", "'导入（会覆盖全部记录）'"),
 ("'Imported — hit Save to store it'", "'已导入 — 点“保存”存下来'"),
 ("'That doesn’t look like a valid backup'", "'这不是有效的备份'"),
 ("btn.textContent = 'sure?'", "btn.textContent = '确定？'"),
 ("btn.textContent = 'clear'", "btn.textContent = '清除'"),
 ("'Give the exercise a name'", "'请给动作起个名字'"),
 ("toast('“'+name+'” added')", "toast('已添加“'+name+'”')"),
 ("toast('Restored')", "toast('已恢复')"),
 ("btn.textContent = 'Delete for good?'", "btn.textContent = '永久删除？'"),
 ("btn.textContent = 'Delete'", "btn.textContent = '删除'"),
 ("toast('“'+(it ? it.n : 'Exercise')+'” deleted, history and all')", "toast('已删除“'+(it ? it.n : '动作')+'”及其记录')"),
 ("toast('“'+item.n+'” moved to '+dayLabel(to))", "toast('“'+item.n+'”已移到'+dayLabel(to))"),
 ("btn.textContent = 'Tap to confirm'", "btn.textContent = '点击确认'"),
 ("btn.textContent = 'Remove'", "btn.textContent = '移除'"),
 ("toast('“'+item.n+'” removed — restore or delete it at the bottom')", "toast('已移除“'+item.n+'” — 可在底部恢复或删除')"),
 ("'File loaded — tap Import twice to replace your log'", "'文件已读取 — 点两次“导入”来替换记录'"),
 ("'this browser is blocking storage'", "'浏览器阻止了存储'"),
 ("variant.bw) return w === 0 ? 'BW' : 'BW+' + w;", "variant.bw) return w === 0 ? '自重' : '自重+' + w;"),
 ("'Main'", "'默认'"),
 ("toast('Give the day a name')", "toast('请给训练日起个名字')"),
]
for a, b in T:
    if a == "toast('Give the day a name')": continue
    if a in ("'Other'",): continue
    if h.count(a) == 0: raise SystemExit('translation source not found: ' + a[:90])
    h = h.replace(a, b)

# first-run banner: only before she has logged anything (no "old app" to move from)
rep("""  } else if (!Object.keys(state.sessions).some(function(k){ return sessionHasContent(state.sessions[k]); })){""",
    """  } else if (!Object.keys(state.sessions).some(function(k){ return sessionHasContent(state.sessions[k]); }) && todayKey() < START){""")

h, n = re.subn(r'版本 [0-9.\-]+', '版本 ' + VERSION, h); assert n == 1
# leftover English check (visible-text heuristics)
left = [s for s in re.findall(r">([^<>{}']*[A-Za-z]{3,}[^<>{}']*)<", h[h.index('</style>'):]) if 'function' not in s and '+' not in s]
print('possible leftovers:', left[:20])

out.mkdir(exist_ok=True)
(out / 'index.html').write_text(h, encoding='utf-8')
shutil.copytree(repo / 'fonts', out / 'fonts', dirs_exist_ok=True)
sw = (repo / 'sw.js').read_text()
sw = re.sub(r"const CACHE = 'ironledger-[^']+';", "const CACHE = 'ironledger-zh-" + VERSION + "';", sw)
sw = sw.replace("return /^ironledger-\\d/.test(k) && k !== CACHE;", "return k.indexOf('ironledger-zh-') === 0 && k !== CACHE;")
sw = sw.replace("  if (url.pathname.indexOf('/zh/') >= 0) return;   /* the Chinese copy has its own worker */\n", "")
assert "/zh/" not in sw
assert "ironledger-zh-') === 0" in sw
(out / 'sw.js').write_text(sw)
import json, subprocess
(out / 'manifest.webmanifest').write_text(json.dumps({"name":"训练记录","short_name":"训练记录","start_url":"./","scope":"./","display":"standalone",
  "background_color":"#EDEEE7","theme_color":"#EDEEE7","icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},
  {"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"any maskable"}]}, ensure_ascii=False, indent=2))
subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('icons.py')), str(out), '#8A3B5C'], check=True)
print('built zh', VERSION)
