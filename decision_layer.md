# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T20:56:46.147365+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VIRTUAL-EUR | action ACHETE_MAINTENANT | opportunité 9.090 | entrée 7.000 | trend 8.150 | rang 8.079
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.908 | entrée 5.800 | trend 9.200 | rang 7.886
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.055 | entrée 7.350 | trend 8.450 | rang 7.851
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 8.079 — opportunité 9.090 — entrée 7.000 — trend 8.150
2. XLM-EUR — ACHETE_MAINTENANT — rank 7.910 — opportunité 8.097 — entrée 7.450 — trend 8.550

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. VIRTUAL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.079
2. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.910
3. AZTEC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.886

## Accélération indépendante

- CELO-EUR — BUILDING_ACCELERATION — score 5.169/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VIRTUAL-EUR — ACTIVE_NOW — score mémoire 8.079/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- HFT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 7.972/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.951/10 — sources ACCELERATION — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 7.910/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 7.886/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 7.851/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- HBAR-EUR +29.70% — DETECTED_EARLY — couche NONE — action NONE
- QNT-EUR +26.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NMR-EUR +16.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +14.80% — DETECTED_EARLY — couche NONE — action NONE
- MIOTA-EUR +9.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LINK-EUR +8.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IKA-EUR +8.78% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +8.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XLM-EUR +5.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +5.78% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
