# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-19T19:09:45.049447+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : KITE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.528 | entrée 5.850 | trend 8.150 | rang 7.083
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : MEGA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.716 | entrée 6.850 | trend 8.850 | rang 7.396
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MEGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.396
2. KITE-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.083
3. CROSS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.861

## Accélération indépendante

- CSPR-EUR — CONFIRMED_ACCELERATION — score 7.456/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — CONFIRMED_ACCELERATION — score 6.641/10 — DETECTED_BUT_TOO_LATE
- SKY-EUR — CONFIRMED_ACCELERATION — score 6.623/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DODO-EUR — BUILDING_ACCELERATION — score 6.393/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RARE-EUR — BUILDING_ACCELERATION — score 5.632/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — BUILDING_ACCELERATION — score 5.337/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TOWNS-EUR — MEMORY_24H — score mémoire 9.889/10 — sources ACCELERATION — MEMORY_ONLY
- ADX-EUR — MEMORY_24H — score mémoire 7.477/10 — sources ACCELERATION — MEMORY_ONLY
- CSPR-EUR — ACTIVE_NOW — score mémoire 7.456/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.396/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- EDGE-EUR — MEMORY_24H — score mémoire 7.201/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 7.083/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 7.000/10 — sources ACCELERATION — MEMORY_ONLY
- CROSS-EUR — ACTIVE_NOW — score mémoire 6.861/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- MMT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.755/10 — sources ACCELERATION — MEMORY_ONLY
- TREAD-EUR — ACTIVE_NOW — score mémoire 6.641/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ICNT-EUR +33.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +26.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +25.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +24.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- YB-EUR +22.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +19.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUNA-EUR +18.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +17.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +16.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +16.00% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
