# Solaire — qualité des horizons du shadow liquidité, 12 octobre 2026

**Statut : correction de mesure seulement.** Le BUY gate, le seuil 75k€/24h, les emails et les ordres ne changent pas.

## Constat sur l'archive figée avant correction

`production_emerging_liquidity_shadow_journal.json` recensait **80 événements**, tous avec un objet `evaluations["4"]`. Pourtant, la distribution de `bars` dans ces évaluations était :

| Nombre de bougies sauvegardées | Événements |
|---|---:|
| 48 | 1 |
| 40–47 | 20 |
| 24–39 | 30 |
| 0–23 | 29 |

Ce comptage n'atteste pas une continuité des timestamps, même pour les événements avec 48 bougies. Les métriques `close_return_pct`, `mfe_pct`, `mae_pct` décrivaient donc parfois une partie seulement de la fenêtre annoncée.

### Risque additionnel de fuite du futur

L'ancien `_eval` sélectionnait les bougies dont **le début** était antérieur au cutoff `t_signal+h`, sans vérifier si leur **clôture** avait eu lieu avant ce cutoff. Pour un signal au milieu d'une tranche de 5 min, la dernière bougie ainsi incluse pouvait se clore **après** la fin de l'horizon annoncé. C'est une fuite temporelle possible des OHLC, indépendamment de la qualité des carnets.

**Un calcul strict** compte uniquement les bougies entières dont le début est postérieur à la bougie contenant le signal ET dont la clôture ne dépasse pas l'horizon. Pour un signal à une heure arbitraire à l'intérieur d'une bougie, cela représente normalement **11** bougies entières à 1h et **47** à 4h, pas les 12/48 tranches idéales d'une fenêtre calée sur la grille. La fenêtre de quelques minutes entre signal et première bougie complète reste non observée par ce calcul.

## Correctif prospectif sur le shadow existant

- Exclure désormais toute bougie dont `start_ms+300000 > horizon_end_ms`.
- Définir une grille attendue des bougies entièrement clôturées **avant** de regarder les cours.
- `COMPLETE_STRICT` uniquement si chaque timestamp attendu apparaît exactement une fois, sans doublon ni timestamp anormal.
- `INCOMPLETE_STRICT` sinon, avec compte des bougies attendues, observées et manquantes.
- Publier `strict_close_return_pct`, `strict_mfe_pct`, `strict_mae_pct` **seulement** si la grille est complète ; dans le cas contraire ils restent `null`.
- Préserver `close_return_pct`, `mfe_pct` et `mae_pct` pour compatibilité, **comme diagnostics potentiellement partiels**, jamais comme performance à horizon fixe si `coverage_status != COMPLETE_STRICT`.
- Les anciens événements ne conservent que le nombre de bougies, pas leurs timestamps. État : `legacy_unverifiable`, sans validation rétrospective artificielle. La nouvelle synthèse `evaluation_coverage` enregistre les nombres de cas complets, incomplets et historiques non vérifiables par horizon.

### Biais restant à traiter

Une bougie absente peut correspondre à l'absence de transaction ou à un trou d'archive : impossible à départager par la seule liste de bougies. Un chemin de bougies complet ne signifie toujours **pas** un fill limite réel ni une sortie au bid exécutable à t+h. Aucun `net_pnl_eur` n'est inféré.

Une évaluation antérieure de 4h ayant pris une bougie après le cutoff ne devient pas valide parce qu'elle possédait 48 records. Les analyses historiques qui l'utilisaient devront être corrigées, ou marquées non comparables, avant de servir à une décision de stratégie.

## Tests ajoutés

- Exclut la mèche d'une bougie se clôturant après le cutoff 1h.
- Refuse les chemins incomplets, dupliqués ou avec timestamp hors-grille.
- Valide un chemin complet de 47 bougies 5min post-signal à 4h, en excluant la mèche future.

Suivi : [issue #134](https://github.com/Vadimrom-create/bitvavo-live/issues/134). Ceci est une correction de **qualité de recherche**, non une promotion du shadow en stratégie live.
