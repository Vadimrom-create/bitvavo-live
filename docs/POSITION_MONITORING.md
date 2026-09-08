# Suivi continu des positions détenues

Ajout demandé lors de la reprise du 8 septembre 2026. Les poids, seuils et règles de classement de la baseline V4 restent inchangés. Le suivi des positions est une couche de gestion distincte, sans prétention de performance V5 démontrée.

## Cycle et décision

À chaque exécution du workflow, après les tests critiques, un checkout isolé lit les soldes et les ordres ouverts Bitvavo, puis les carnets et bougies des positions détenues. Cette étape s’exécute même si la prospection échoue. Une position hors top V4 est contrôlée également. Seuls les marchés EUR actuellement négociables et les soldes spot accessibles par `/balance` sont couverts ; les actifs retirés, marchés suspendus ou produits distincts produisent un contrôle incomplet.

| Action | Justification requise | Principaux blocages |
|---|---|---|
| ACHÈTE | Achat V4 admissible, relecture validée, publication réussie, carnet récent, prix à moins de 0,5 % du signal, plan recalculé avec le solde réel | Position déjà détenue, ordre d’achat ouvert, risque/exposition/cash indisponible ou dépassé, corrélation forte ou inconnue, données insuffisantes |
| VENDS | Prix acheteur récent inférieur ou égal au stop vérifié de la position | Solde ou carnet périmé, plan incohérent, ordre de sortie équivalent déjà présent |
| PRENDS PARTIELLEMENT TES PROFITS | TP1 privé vérifié atteint, résultat estimé net positif, minimums respectés, spread ≤1 % | TP1 déjà confirmé, quantité déjà réduite au reliquat prévu, ordre limite équivalent déjà exécutable |
| RELÈVE LE STOP | Support de bougies 15m closes valides et fraîches, buffer ATR, niveau supérieur au stop actuel et au seuil net de rentabilité | Structure absente, amélioration <max(0,5 ATR, 2 ticks), nouveau niveau inférieur à la dernière proposition, délai d’une heure |

Priorité par position : sortie, profits partiels, stop, achat. Sans justification, **aucun email**. Un stop n’est jamais abaissé. Un stop proposé n’est jamais enregistré comme exécuté. Le franchissement d’un stop peut être contrôlé même sans historique de bougies ; il exige un carnet récent. Un stop-limit potentiellement bloqué ne suffit pas à supprimer une alerte de sortie. Les ordres de vente concurrents sont signalés dans l’email pour vérification humaine.

Le solde doit dater de 120 secondes au plus et le carnet de 90 secondes au plus. Ces conditions sont revérifiées avant l’envoi. L’adaptateur refuse toute route autre que GET `/balance` et GET `/ordersOpen`, ainsi que les redirections HTTP. Aucun ordre, annulation ou retrait n’est possible par ce module.

## Activation privée

Configurer dans les **GitHub Actions Secrets**, jamais dans un fichier public ou un message :

| Secret | Contenu |
|---|---|
| `BITVAVO_READ_API_KEY` | Clé Bitvavo dédiée avec permission de consultation uniquement |
| `BITVAVO_READ_API_SECRET` | Secret associé à cette clé |
| `POSITION_STATE_KEY` | Clé Fernet créée une fois et conservée pour relire l’état chiffré |
| `POSITION_PLANS_JSON` | Objet JSON des plans de gestion vérifiés, indexé par marché |

Conserver `GMAIL_APP_PASSWORD` et la variable `ALERT_GMAIL_USER` existants. Le destinataire autorisé est `bellonirom@gmail.com`. Aucun test d’envoi n’est exécuté automatiquement.

La clé d’état peut être générée localement avec `python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'`, puis saisie directement dans GitHub Secrets. Ne pas lancer cette commande dans un log public. Ne pas changer cette clé sans migrer le registre : une clé incorrecte interrompt les notifications au lieu de réinitialiser la déduplication.

Exemple de schéma **fictif, à remplacer par les données réellement vérifiées** :

```json
{
  "EXAMPLE-EUR": {
    "position_id": "identifiant-unique-de-cette-ouverture",
    "verified": true,
    "initial_amount": 10,
    "cost_basis_eur": 10,
    "stop_eur": 9,
    "tp1_eur": 15,
    "tp1_fraction": 0.5,
    "tp1_done": false,
    "fee_rate": 0.0025,
    "slippage_rate": 0.001
  }
}
```

Le coût unitaire, le stop et les objectifs doivent venir du suivi réel de la position. `/balance` ne fournit pas de prix de revient ; quelques transactions récentes ne prouvent pas le coût complet. Mettre à jour le plan après un ajout, une modification exécutée du stop ou un changement de scénario. Une quantité supérieure à la quantité initiale invalide le plan. Une réduction au reliquat prévu évite de reproposer TP1. Une clôture puis réouverture observée exige un nouvel identifiant. Une clôture/réouverture intégralement entre deux cycles et de même quantité n’est pas détectable par les seuls soldes : le plan doit alors être renouvelé explicitement.

Les frais et le glissement sont des hypothèses configurables ; les quantités de l’email restent des propositions à confronter à la profondeur réellement disponible. Le carnet n’assure pas un prix d’exécution. Aucune probabilité de gain n’est attribuée à ces règles.

## Confidentialité, état et limites

Les positions, quantités et marqueurs de livraison restent en mémoire ou dans `position_alert_state.enc.json`, chiffré et authentifié avec Fernet. Aucune réponse privée brute ne rejoint les journaux de marché, artifacts de replay, GitHub Pages ou logs. Le statut public indique uniquement `UNCONFIGURED`, `OK`, `PARTIAL`, `STALE` ou `ERROR`, et la disponibilité de l’envoi. `UNCONFIGURED` ne signifie jamais « aucune position ».

Une erreur sur un marché n’empêche pas le contrôle des autres positions. Tout risque de portefeuille inconnu bloque un nouvel achat. Les sorties urgentes ne sont pas bloquées par le cooldown des achats. Un TP1 ou un franchissement du même stop n’est notifié qu’une fois par identifiant de position ; réviser le plan et son identité pour réarmer un scénario explicitement renouvelé.

L’état de livraison change après le retour réussi de SMTP. Un échec d’envoi reste réessayable. Une panne après acceptation SMTP mais avant la publication de l’état demeure une fenêtre de doublon possible ; l’outil n’annonce pas une garantie d’exactement une livraison.

« Continu » signifie **à chaque cycle effectivement exécuté**, pas surveillance seconde par seconde. GitHub Actions peut retarder ou omettre des exécutions cron. Les emails ne remplacent donc pas un ordre de protection réellement placé. Pour une cadence stricte, déployer le même module sur un service privé persistant avec adresse IP autorisée par Bitvavo et supervision indépendante ; aucun serveur de ce type n’a été inventé ou activé dans ce travail.

## Sources API

- [Authentification REST Bitvavo](https://docs.bitvavo.com/docs/rest-api/introduction/)
- [Soldes disponibles et engagés](https://docs.bitvavo.com/docs/rest-api/get-account-balance/)
- [Ordres ouverts](https://docs.bitvavo.com/docs/rest-api/get-open-orders/)
- [Bougies et périodes sans transaction](https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/)
- [Limites de programmation GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
