# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T21:34:44.439439+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VIRTUAL-EUR | action ACHETE_MAINTENANT | opportunité 9.154 | entrée 8.250 | trend 9.000 | rang 8.630
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : DRIFT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.031 | entrée 5.850 | trend 7.550 | rang 7.294
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.819 | entrée 5.200 | trend 7.900 | rang 7.009
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : RUNE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.076 | entrée 6.300 | trend 8.900 | rang 7.808
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.630 — opportunité 9.154 — entrée 8.250 — trend 9.000

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.630
2. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.808
3. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.797

## Accélération indépendante

- FUEL-EUR — BUILDING_ACCELERATION — score 5.846/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.630/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 7.972/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.844/10 — sources ACCELERATION — MEMORY_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.808/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.797/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 7.742/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +30.82% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +14.57% — DETECTED_EARLY — couche NONE — action NONE
- NMR-EUR +13.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +10.08% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +9.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +9.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LINK-EUR +8.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +6.85% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- DGB-EUR +6.64% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AZTEC-EUR +6.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
