# Solaire downstream correction — 25 septembre 2026

## Décision

Le scanner d'accélération reste gelé. Les corrections de ce lot ciblent la chaîne aval :
détection -> sélection/décision -> exécution -> gestion de position.

Les cas de la journée montrent qu'une partie importante de la valeur est perdue après la détection,
soit parce qu'un momentum fort est déclassé comme "trop tard", soit parce qu'une nouvelle
accélération est assimilée à un ancien BUY, soit parce qu'un stop est resserré avant que le trade
ait réellement monétisé son avantage.

## Éléments observés avant correction

- PHA avait déjà généré un BUY de production autour de 0,046256 EUR (signal autour de 0,046652 EUR).
  Plus tard, une nouvelle accélération (épisode 33) a été rejetée avec
  `PRIOR_BUY_THESIS_STILL_ACTIVE` alors que le dernier épisode envoyé était le 24.
- AERO avait déjà généré un BUY de production autour de 0,67746 EUR.
- La Decision Layer déclarait dans ses principes que le timing/chase n'était pas un veto, mais
  `category == "TOO LATE"` bloquait encore les buckets achat immédiat et limite passive.
- L'ordre des alertes privilégiait lexicographiquement la plus faible extension avant la force du
  signal, ce qui pouvait déclasser une vraie continuation.
- Les plans de risque avaient déjà un stop structurel et un sizing lié au risque. Le défaut à
  corriger n'est donc pas de supprimer le stop initial, mais d'éviter de le resserrer trop tôt.
- La couche de gestion de positions sait produire `PRENDS PARTIELLEMENT TES PROFITS` et
  `RELÈVE LE STOP`, mais le monitoring de compte est actuellement non configuré ; il ne peut donc
  pas gérer les positions réelles aujourd'hui.

## Modifications

1. **TOO LATE n'est plus un veto.** Il devient un drapeau de risque/timing. Une structure buy-ready
   peut rester achetable ; l'extension continue de pénaliser le ranking.
2. **Nouvel épisode = nouvelle information.** Un ancien BUY encore théoriquement valide ne peut plus
   supprimer un épisode d'accélération ultérieur.
3. **Ranking des alertes.** Force du signal puis preuves d'accélération passent avant l'extension ;
   l'extension reste un tiebreaker de risque.
4. **TP = gestion, pas liquidation automatique.** Les niveaux 2R/3R restent disponibles pour les
   études mais sont présentés comme seuil de réévaluation/prise partielle puis référence runner.
5. **Pas de stop relevé avant prise partielle.** Le gestionnaire de positions conserve le stop
   structurel initial tant qu'une première prise de bénéfice n'a pas été constatée. Après la
   partielle, le stop du runner peut être remonté sous un support confirmé.

## Ce qui ne change pas

- Aucun seuil du scanner d'accélération n'est modifié.
- Aucun ordre n'est envoyé automatiquement.
- Le stop initial reste structurel et le sizing reste limité par le risque en euros.
- Les études de politiques de sortie restent prospectives ; leurs petits échantillons ne sont pas
  utilisés pour choisir rétroactivement un objectif fixe "optimal".

## Critère de validation

Le lot doit réduire les faux négatifs aval et la capture prématurée des gagnants sans augmenter
mécaniquement le risque en euros. Les métriques à suivre restent : sélection retenue/rejetée, MFE,
MAE, sortie réelle, fraction de MFE capturée et PnL net.
