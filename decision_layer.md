# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T15:58:12.901872+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.389 | entrée 6.800 | trend 8.900 | rang 8.007
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : XDC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.515 | entrée 5.950 | trend 8.450 | rang 7.422
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.832 | entrée 4.950 | trend 8.900 | rang 7.605
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.261 | entrée 6.450 | trend 8.450 | rang 8.288
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.007 — opportunité 8.389 — entrée 6.800 — trend 8.900
2. STX-EUR — ACHETE_MAINTENANT — rank 7.607 — opportunité 8.495 — entrée 7.200 — trend 8.950
3. BTC-EUR — ACHETE_MAINTENANT — rank 6.662 — opportunité 8.251 — entrée 7.600 — trend 5.350
4. TRX-EUR — ACHETE_MAINTENANT — rank 5.874 — opportunité 8.105 — entrée 7.250 — trend 3.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.288
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.007
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.973

## Accélération indépendante

- XYO-EUR — CONFIRMED_ACCELERATION — score 7.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOVR-EUR — CONFIRMED_ACCELERATION — score 6.830/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 6.044/10 — DETECTED_BUT_TOO_LATE
- NOM-EUR — BUILDING_ACCELERATION — score 5.991/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.574/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALICE-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE
- AUDIO-EUR — BUILDING_ACCELERATION — score 5.447/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLM-EUR — BUILDING_ACCELERATION — score 5.361/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NIL-EUR — BUILDING_ACCELERATION — score 5.071/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — BUILDING_ACCELERATION — score 5.007/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.007/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.594/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 8.288/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MEGA-EUR — MEMORY_24H — score mémoire 8.157/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AVAX-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 7.877/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +110.40% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +70.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CAP-EUR +32.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ALICE-EUR +27.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +22.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NOS-EUR +21.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +20.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEGA-EUR +19.83% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +19.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVE-EUR +14.42% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
