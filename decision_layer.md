# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-05T21:24:02.216605+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 8.051 | entrée 7.750 | trend 9.200 | rang 7.937
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : C-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.550 | entrée 6.000 | trend 8.950 | rang 7.475
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 7.679 | entrée 5.750 | trend 8.850 | rang 7.207
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : BAT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.153 | entrée 6.550 | trend 8.900 | rang 7.782
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. FET-EUR — ACHETE_MAINTENANT — rank 7.937 — opportunité 8.051 — entrée 7.750 — trend 9.200
2. WLD-EUR — ACHETE_MAINTENANT — rank 7.619 — opportunité 8.100 — entrée 7.600 — trend 8.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.937
2. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.782
3. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.648

## Accélération indépendante

- API3-EUR — CONFIRMED_ACCELERATION — score 8.807/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 8.233/10 — DETECTED_BUT_TOO_LATE
- RAD-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- ZKJ-EUR — BUILDING_ACCELERATION — score 5.939/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 5.936/10 — DETECTED_BUT_TOO_LATE
- MOVR-EUR — BUILDING_ACCELERATION — score 5.558/10 — DETECTED_BUT_TOO_LATE
- RLC-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- IRYS-EUR — BUILDING_ACCELERATION — score 5.376/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WLD-EUR — BUILDING_ACCELERATION — score 5.257/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEOPLE-EUR — BUILDING_ACCELERATION — score 4.881/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 7.619/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- EDU-EUR — MEMORY_24H — score mémoire 9.962/10 — sources ACCELERATION — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- API3-EUR — ACTIVE_NOW — score mémoire 8.807/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SWELL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.525/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZKP-EUR — MEMORY_24H — score mémoire 8.310/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — ACTIVE_NOW — score mémoire 8.233/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- PORTAL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.189/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- RLC-EUR +84.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +76.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAD-EUR +31.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +29.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +23.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +21.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVR-EUR +16.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDU-EUR +16.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +15.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CARV-EUR +14.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
