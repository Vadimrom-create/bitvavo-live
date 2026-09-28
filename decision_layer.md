# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T23:50:11.127729+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VIRTUAL-EUR | action ACHETE_MAINTENANT | opportunité 8.990 | entrée 7.000 | trend 9.000 | rang 8.341
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.877 | entrée 6.000 | trend 8.400 | rang 7.540
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CRV-EUR | action LATENT_ACCELERATOR | opportunité 8.158 | entrée 5.750 | trend 8.450 | rang 7.328
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : CRO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.221 | entrée 7.000 | trend 8.450 | rang 8.297
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.341 — opportunité 8.990 — entrée 7.000 — trend 9.000
2. XDC-EUR — ACHETE_MAINTENANT — rank 8.031 — opportunité 8.097 — entrée 7.100 — trend 9.000
3. XLM-EUR — ACHETE_MAINTENANT — rank 8.022 — opportunité 8.488 — entrée 7.300 — trend 8.800
4. BCH-EUR — ACHETE_MAINTENANT — rank 8.004 — opportunité 9.074 — entrée 7.650 — trend 7.550
5. RENDER-EUR — ACHETE_MAINTENANT — rank 7.835 — opportunité 8.775 — entrée 7.500 — trend 7.850
6. ETC-EUR — ACHETE_MAINTENANT — rank 7.415 — opportunité 7.997 — entrée 7.350 — trend 7.400

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.341
2. CRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.297
3. XDC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.031

## Accélération indépendante

- AUCTION-EUR — CONFIRMED_ACCELERATION — score 7.106/10 — DETECTED_BUT_TOO_LATE
- TRB-EUR — BUILDING_ACCELERATION — score 6.389/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIO-EUR — BUILDING_ACCELERATION — score 6.162/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — BUILDING_ACCELERATION — score 6.069/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MLN-EUR — BUILDING_ACCELERATION — score 5.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FRAX-EUR — BUILDING_ACCELERATION — score 5.443/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTR-EUR — BUILDING_ACCELERATION — score 5.218/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 5.103/10 — DETECTED_BUT_TOO_LATE
- WELL-EUR — BUILDING_ACCELERATION — score 5.098/10 — DETECTED_BUT_TOO_LATE
- MMT-EUR — BUILDING_ACCELERATION — score 4.964/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.341/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XLM-EUR — ACTIVE_NOW — score mémoire 8.022/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.275/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CRO-EUR — ACTIVE_NOW — score mémoire 8.297/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 8.031/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BCH-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRASS-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- NMR-EUR +43.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +26.84% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +12.99% — DETECTED_EARLY — couche NONE — action NONE
- LINK-EUR +9.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- 0G-EUR +9.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +9.08% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- CRV-EUR +8.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XLM-EUR +7.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MIOTA-EUR +6.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREAD-EUR +6.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
