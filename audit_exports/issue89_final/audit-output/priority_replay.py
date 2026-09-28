from replay import *
events=[
 ('KMNO21','KMNO-EUR','2026-09-21T02:52:35+00:00',.029925,.02822),
 ('TREAD21','TREAD-EUR','2026-09-21T10:05:02+00:00',.38501,.36549),
 ('TREAD22','TREAD-EUR','2026-09-22T18:47:44+00:00',.470,.43311),
 ('KMNO24','KMNO-EUR','2026-09-24T02:34:36+00:00',.032992,.030626),
 ('QNT24','QNT-EUR','2026-09-24T13:59:26+00:00',69.091,62.916)]
result=[];db=sqlite3.connect(OUT/'bars.sqlite')
for label,market,t,entry,stop in events:
 e=dict(id=label,source='EMAIL_AVAILABLE',market=market,ts=datetime.fromisoformat(t).timestamp(),quote=entry,stop=stop,score=0)
 for n in (100,150):
  result.append(simulate('isolated_'+label,[e],n,4,db))
save('priority_isolated_metrics',result)
