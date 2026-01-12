<div dir="rtl" align="right">

# 📖 DevOps Quick Reference - מאגר מידע מהיר

> **Ctrl+F Friendly** - כל תשובה קצרה, ברורה, עם יתרונות/חסרונות ושימושים

---

# ☁️ AWS - שירותי ענן

---

## IAM - ניהול זהויות

### IAM USER vs IAM ROLE

| מאפיין | IAM User | IAM Role |
|--------|----------|----------|
| **מה זה** | זהות לאדם | זהות לשירות/אפליקציה |
| **אימות** | Username + Password / Access Keys | Assume Role (זמני) |
| **תוקף** | קבוע | זמני (מתחלף אוטומטית) |
| **שימוש** | מפתח נכנס ל-Console | EC2 ניגש ל-S3 |
| **Best Practice** | לאנשים בלבד | לכל דבר אוטומטי |

**כלל: לשירותים תמיד Role, לא User!**

---

### IAM POLICY vs RESOURCE BASED POLICY

| מאפיין | IAM Policy | Resource Based Policy |
|--------|------------|----------------------|
| **מוצמד ל** | User / Group / Role | המשאב עצמו (S3, SQS) |
| **שואל** | "מה המשתמש יכול?" | "מי יכול לגשת למשאב?" |
| **Cross-Account** | דורש Assume Role | ישיר - פשוט יותר |
| **דוגמה** | "יכול לקרוא מכל S3" | "Bucket מאפשר לחשבון X" |

---

## VPC - רשתות

### VPC - מה זה?

**VPC** = Virtual Private Cloud = הרשת הפרטית שלך ב-AWS.

**מה מגדירים:**
- טווח IPs (CIDR)
- Subnets (Public/Private)
- Route Tables
- Security Groups

---

### SUBNET פרטי vs ציבורי

| מאפיין | Public Subnet | Private Subnet |
|--------|---------------|----------------|
| **גישה לאינטרנט** | ישירה דרך IGW | רק דרך NAT |
| **IP ציבורי** | כן | לא |
| **Route Table** | מצביע ל-Internet Gateway | מצביע ל-NAT Gateway |
| **מה שמים שם** | ALB, Web Servers, Bastion | Database, Backend, Internal |

---

### INTERNET GATEWAY

**מה זה:** שער שמחבר VPC לאינטרנט.

**מאפיינים:**
- מאפשר תנועה נכנסת ויוצאת
- Highly Available (AWS מנהל)
- חינמי (משלמים רק Data Transfer)
- חייב להיות ב-Public Subnet

---

### NAT GATEWAY

**מה זה:** מאפשר ל-Private Subnet לצאת לאינטרנט בלי להיחשף.

**מאפיינים:**
- יציאה בלבד - אי אפשר להיכנס!
- יושב ב-Public Subnet
- עולה כסף (~$0.045/שעה + Data)
- שימוש: עדכוני תוכנה, API calls

---

### PRIVATE LINK / VPC ENDPOINT

**מה זה:** גישה לשירותי AWS בלי לעבור דרך האינטרנט.

| סוג | מה זה | עלות | שימוש |
|-----|-------|------|-------|
| **Interface Endpoint** | ENI בתוך ה-VPC | בתשלום | רוב השירותים |
| **Gateway Endpoint** | Route Table entry | חינם! | S3, DynamoDB בלבד |

**יתרונות:**
- אבטחה - Traffic לא יוצא מ-AWS
- ביצועים - Latency נמוך
- עלות - חוסך NAT Gateway

---

### SG REFERENCING

**מה זה:** התייחסות ל-Security Group אחר במקום CIDR.

**במקום:**
```
Inbound: Allow 10.0.0.0/16 (כל ה-VPC)
```

**עדיף:**
```
Inbound: Allow sg-alb-12345 (רק ה-ALB)
```

**יתרון:** יותר מאובטח, יותר ספציפי, דינמי.

---

## Storage - אחסון

### EBS vs EFS

| מאפיין | EBS | EFS |
|--------|-----|-----|
| **סוג** | Block Storage (דיסק) | File Storage (NFS) |
| **חיבור** | EC2 אחד בלבד | מרובה EC2 |
| **AZ** | באותו AZ בלבד | Cross-AZ |
| **Scaling** | ידני | אוטומטי |
| **מחיר** | זול יותר | יקר יותר |
| **שימוש** | Database, Boot | Shared files, CMS |

---

### S3

**מה זה:** Object Storage - אחסון קבצים ללא הגבלה.

**מאפיינים:**
- Unlimited capacity
- 99.999999999% Durability (11 תשיעיות)
- Versioning
- Encryption
- Lifecycle policies

**Storage Classes:**
| Class | זמינות | מחיר | שימוש |
|-------|--------|------|-------|
| Standard | מיידי | גבוה | גישה תכופה |
| IA | מיידי | בינוני | גישה לא תכופה |
| Glacier | דקות-שעות | נמוך | ארכיון |
| Deep Archive | 12-48 שעות | הכי זול | ארכיון ארוך |

---

## Compute - מחשוב

### EC2 PURCHASING OPTIONS

| סוג | מה זה | הנחה | מתי להשתמש |
|-----|-------|------|------------|
| **On-Demand** | לפי שעה, ללא התחייבות | 0% | Dev, Testing, Unpredictable |
| **Reserved** | התחייבות 1-3 שנים | עד 72% | Production, Steady workloads |
| **Spot** | קיבולת עודפת, יכול להיפסק | עד 90% | Batch, CI/CD, Flexible |
| **Dedicated Host** | שרת פיזי שלם לך | תלוי | Compliance, Licensing |

**כלל:** Production = Reserved, Dev = On-Demand, Batch = Spot

---

### LAMBDA

**מה זה:** Serverless - מריץ קוד בלי לנהל שרתים.

**מאפיינים:**
- Event-driven
- Pay per millisecond
- Auto-scale
- Max 15 minutes timeout
- Max 10GB memory

**מתזמן טריגרים:** Amazon EventBridge (Cron, Rate, Events)

---

## Load Balancing

### סוגי LOAD BALANCER

| סוג | שכבה | פרוטוקול | שימוש |
|-----|------|----------|-------|
| **ALB** | Layer 7 | HTTP/HTTPS | Web apps, Microservices, Path routing |
| **NLB** | Layer 4 | TCP/UDP | High performance, Gaming, IoT |
| **GLB** | Layer 3 | IP | Firewalls, Security appliances |

**כלל:** Web = ALB, Performance = NLB

---

## DNS & CDN

### ROUTE 53 - DNS

**מה זה:** שירות DNS של AWS. מתרגם domain → IP.

**סוגי ניתוב:**

| סוג | לוגיקה | שימוש |
|-----|--------|-------|
| **Simple** | IP אחד | Basic |
| **Weighted** | לפי אחוזים | A/B Testing, Canary |
| **Latency** | הכי מהיר למשתמש | ביצועים |
| **Geolocation** | לפי מיקום גאוגרפי | Compliance, Content localization |
| **Failover** | Primary/Secondary | DR |

---

### CLOUDFRONT - CDN

**מה זה:** Content Delivery Network - מפיץ תוכן ל-Edge Locations.

**יתרונות:**
- Latency נמוך למשתמשים רחוקים
- Caching - חוסך עומס מה-Origin
- SSL/TLS מובנה
- WAF integration
- DDoS protection

---

### ACM - SSL/TLS

**מה זה:** AWS Certificate Manager - ניהול תעודות SSL.

**עלות:** חינם!

**מאפיינים:**
- חידוש אוטומטי
- עובד עם: ALB, CloudFront, API Gateway
- לא עובד ישירות עם EC2

---

## Database

### רלציוני vs לא-רלציוני

| מאפיין | Relational (SQL) | Non-Relational (NoSQL) |
|--------|------------------|------------------------|
| **מבנה** | טבלאות, שורות, עמודות | Documents, Key-Value, Graph |
| **Schema** | קבוע מראש | גמיש |
| **Scaling** | בעיקר Vertical | בעיקר Horizontal |
| **קשרים** | JOINs מורכבים | פשוט יותר |
| **AWS** | RDS, Aurora | DynamoDB, DocumentDB |
| **שימוש** | טרנזקציות, קשרים | Big Data, Real-time |

---

### REDIS

**מה זה:** In-memory key-value store.

**מאפיינים:**
- מהיר מאוד (הכל בזיכרון)
- Caching
- Session storage
- Pub/Sub
- Leaderboards

**AWS:** ElastiCache for Redis

---

### STANDBY DB vs PRIMARY DB

| סוג | תפקיד | אפשר לקרוא? |
|-----|-------|-------------|
| **Primary (Master)** | Write + Read | כן |
| **Standby (Multi-AZ)** | Failover בלבד | לא! |
| **Read Replica** | Read בלבד | כן |

**Standby = גיבוי חם, לא לקריאה!**

---

## Scaling

### VERTICAL vs HORIZONTAL SCALING

| מאפיין | Vertical (Scale Up) | Horizontal (Scale Out) |
|--------|---------------------|------------------------|
| **מה עושים** | מגדילים את המכונה | מוסיפים עוד מכונות |
| **דוגמה** | t3.small → t3.xlarge | 1 instance → 10 instances |
| **גבול** | יש מקסימום | כמעט ללא גבול |
| **Downtime** | בדרך כלל כן | לא |
| **מתאים ל** | Databases | Stateless apps |

---

## Decoupled Services

**מה זה:** שירותים שלא תלויים ישירות אחד בשני.

**במקום:**
```
Service A → Service B (ישיר)
```

**עדיף:**
```
Service A → Queue (SQS) → Service B
```

**יתרונות:**
- אם B נופל, A ממשיך
- Async processing
- Better scaling
- Fault tolerance

---

# ☸️ KUBERNETES

---

## Core Concepts

### NAMESPACE

**מה זה:** חלוקה לוגית של הקלאסטר.

**שימושים:**
- הפרדה בין סביבות (dev, staging, prod)
- הפרדה בין צוותים
- Resource Quotas

**Default namespaces:** default, kube-system, kube-public

---

### DEPLOYMENT vs REPLICASET

| מאפיין | ReplicaSet | Deployment |
|--------|------------|------------|
| **תפקיד** | שומר על מספר Pods | מנהל ReplicaSets |
| **Rolling Update** | ❌ | ✅ |
| **Rollback** | ❌ | ✅ |
| **History** | ❌ | ✅ |
| **שימוש ישיר** | כמעט אף פעם | תמיד! |

**כלל:** תמיד Deployment, לא ReplicaSet ישירות.

---

### INGRESS vs INGRESS CONTROLLER

| רכיב | מה זה | דוגמה |
|------|-------|-------|
| **Ingress** | Resource (YAML) - חוקי ניתוב | hosts, paths |
| **Ingress Controller** | התוכנה שאוכפת | NGINX, Traefik, HAProxy |

**משל:** Ingress = תמרור, Controller = שוטר

---

### סוגי CONTAINERS

| סוג | מתי רץ | תפקיד | דוגמה |
|-----|--------|-------|-------|
| **Init** | לפני Main | הכנות | הורדת קבצים, המתנה ל-DB |
| **Application** | אחרי Init | האפליקציה | Web server |
| **Sidecar** | במקביל ל-Main | עזר | Logging, Proxy, Monitoring |

---

### PROBES

| Probe | שואל | אם נכשל |
|-------|------|---------|
| **Liveness** | "אתה חי?" | Restart container |
| **Readiness** | "אתה מוכן לTraffic?" | לא שולחים בקשות |
| **Startup** | "עלית?" | ממתינים (לאפליקציות איטיות) |

---

### SERVICE ACCOUNT

**מה זה:** זהות עבור Pods (לא בני אדם).

**שימושים:**
- תקשורת עם Kubernetes API
- RBAC permissions
- קישור ל-AWS IAM (IRSA)

---

### PVC - PERSISTENT VOLUME CLAIM

**מה זה:** בקשה לאחסון.

| רכיב | תפקיד |
|------|-------|
| **PV** (Persistent Volume) | האחסון הפיזי |
| **PVC** (Claim) | הבקשה - "אני צריך 10GB" |
| **StorageClass** | סוג האחסון (SSD, HDD) |

**משל:** PV = דירה, PVC = חוזה שכירות

---

### HPA - AUTOSCALING

**מה זה:** Horizontal Pod Autoscaler.

**איך עובד:**
1. מודד metrics (CPU, Memory, Custom)
2. משווה ל-target (70%)
3. מוסיף/מוריד Pods

**הגדרות:**
- minReplicas
- maxReplicas
- targetCPUUtilization

---

## Workload Types

### DEPLOYMENT vs STATEFULSET vs DAEMONSET

| סוג | מה זה | זהות Pods | שימוש |
|-----|-------|-----------|-------|
| **Deployment** | Stateless apps | אקראית, חלופית | Web servers, APIs |
| **StatefulSet** | Stateful apps | קבועה (pod-0, pod-1) | Databases, Kafka |
| **DaemonSet** | Pod על כל Node | לפי Node | Logging, Monitoring |

---

### סוגי SERVICES

| סוג | נגישות | שימוש |
|-----|--------|-------|
| **ClusterIP** | רק מתוך הקלאסטר | Internal services (ברירת מחדל) |
| **NodePort** | Port על כל Node (30000-32767) | Dev/Testing |
| **LoadBalancer** | Cloud LB חיצוני | Production |
| **ExternalName** | DNS CNAME | גישה לשירות חיצוני |

---

### 4 סוגי פריסות (DEPLOYMENT STRATEGIES)

| סוג | איך עובד | Downtime | Rollback | מתי |
|-----|----------|----------|----------|-----|
| **Rolling Update** | מחליף Pod אחד בכל פעם | ❌ אין | מהיר | ברירת מחדל |
| **Recreate** | מוחק הכל → מעלה חדש | ✅ יש | מהיר | כשאי אפשר 2 גרסאות |
| **Blue-Green** | סביבה חדשה מלאה → Switch | ❌ אין | מיידי | כשצריך rollback מהיר |
| **Canary** | % קטן מהמשתמשים קודם | ❌ אין | מהיר | בדיקה ב-Production |

---

### ISTIO

**מה זה:** Service Mesh - שכבת ניהול תקשורת בין שירותים.

**יכולות:**
- Traffic Management (routing, load balancing)
- Security (mTLS בין services)
- Observability (metrics, tracing, logging)

**איך עובד:** Sidecar proxy (Envoy) לכל Pod

---

## HELM

### מה זה HELM?

**מה זה:** Package Manager לקוברנטיס (כמו apt/yum).

**למה צריך:**
- Templating - YAMLים דינמיים
- Packaging - חבילות מוכנות
- Versioning - ניהול גרסאות
- Rollback - חזרה לגרסה קודמת

**מבנה Chart:**
```
mychart/
├── Chart.yaml      # Metadata
├── values.yaml     # Default values
└── templates/      # K8s YAMLs with {{ }}
```

---

### HELM LINT

**מה זה:** בודק תקינות Chart לפני התקנה.

```bash
helm lint ./my-chart
```

**בודק:** Syntax, Best practices, Required fields

---

### _HELPERS.TPL

**מה זה:** קובץ עם פונקציות לשימוש חוזר.

**למה:** DRY - לא לחזור על אותו קוד

**דוגמה:**
```yaml
{{- define "mychart.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}
```

---

# 🔄 CI/CD

---

## CI vs CD

| מונח | משמעות | מה כולל |
|------|--------|---------|
| **CI** | Continuous Integration | Build, Test, Lint - על כל commit |
| **CD** | Continuous Delivery | פריסה אוטומטית לסביבות |

---

## ARTIFACT

**מה זה:** תוצר של תהליך Build.

**דוגמאות:**
- Docker Image
- JAR/WAR file
- Compiled binary
- Test reports

**איפה שומרים:** Artifactory, Nexus, S3, ECR

---

## שלבי CI/CD

```
1. Source      → Code checkout
2. Build       → Compile, npm install
3. Test        → Unit, Integration, E2E
4. Package     → Docker build, Create artifact
5. Deploy      → Push to environment
6. Verify      → Health checks, Smoke tests
```

---

## GITHUB ACTIONS vs JENKINS

| מאפיין | GitHub Actions | Jenkins |
|--------|----------------|---------|
| **סוג** | SaaS (מנוהל) | Self-hosted |
| **תחזוקה** | GitHub | אתה |
| **עלות** | דקות חינם + תשלום | חינם (+ שרתים) |
| **גמישות** | טובה | מקסימלית |
| **Plugins** | Actions Marketplace | הרבה מאוד |
| **קובץ** | YAML | Groovy (Jenkinsfile) |

---

## GITHUB vs GITLAB

| מאפיין | GitHub | GitLab |
|--------|--------|--------|
| **CI/CD** | Actions | CI מובנה יותר |
| **Self-hosted** | Enterprise (יקר) | Community (חינם) |
| **Container Registry** | Packages | מובנה |
| **DevOps Platform** | אינטגרציות | All-in-one |

---

## הרצה ידנית בין שלבים (JENKINS)

**כן אפשר!** עם `input` step:

```groovy
stage('Deploy') {
    steps {
        input message: 'Deploy to prod?', ok: 'Deploy!'
        sh './deploy.sh'
    }
}
```

---

# 🏗️ TERRAFORM

---

## DRIFT

**מה זה:** פער בין State לבין המצב האמיתי בענן.

**למה קורה:** מישהו שינה ידנית ב-Console.

**איך מזהים:** `terraform plan`

**איך מתקנים:** `terraform apply`

---

## שינוי שם BUCKET

**שאלה:** אם נערוך שם Bucket ב-Terraform?

**תשובה:** ימחק את הישן ויצור חדש!

**למה:** שם Bucket הוא immutable - לא ניתן לשינוי.

**זהירות:** אפשר לאבד נתונים!

---

## TERRAFORM VALIDATE

**מה זה:** בודק תקינות קבצי .tf

```bash
terraform validate
```

**בודק:** Syntax, Types, Required args

**לא בודק:** מול הענן - רק את הקוד!

---

## STATE - איפה לשמור?

**תשובה:** Remote Backend - S3 + DynamoDB

**למה:**
- שיתוף בין חברי צוות
- Locking - מניעת שינויים במקביל
- גיבוי ואבטחה

**לא לשמור ב-Git!** (מידע רגיש)

---

## TERRAFORM WORKSPACE

**מה זה:** States נפרדים לאותו קוד.

```bash
terraform workspace new dev
terraform workspace new prod
terraform workspace select dev
```

**שימוש:** dev, staging, prod מאותו קוד

---

## MODULE

**מה זה:** קבוצת Resources לשימוש חוזר.

**כמו:** פונקציה - מקבל inputs, מחזיר outputs

**יתרון:** DRY - Don't Repeat Yourself

---

## CLOUDFORMATION vs TERRAFORM

| מאפיין | CloudFormation | Terraform |
|--------|----------------|-----------|
| **ספק** | AWS בלבד | Multi-cloud |
| **שפה** | JSON/YAML | HCL |
| **State** | AWS מנהל | אתה מנהל |
| **Learning** | קל יותר ל-AWS | גמיש יותר |

---

## OIDC - GITHUB ל-AWS

**מה זה:** אימות בלי Access Keys!

**שלבים:**
1. Identity Provider ב-AWS (GitHub)
2. IAM Role עם Trust Policy
3. בWorkflow: `aws-actions/configure-aws-credentials`

**יתרון:** אין secrets לנהל!

---

# 📊 MONITORING

---

## PROMETHEUS

**מה זה:** מערכת Monitoring ואיסוף Metrics.

**מאפיינים:**
- Pull-based (מושך metrics)
- Time-series DB
- PromQL (שפת שאילתות)
- Alerting מובנה

---

## GRAFANA

**מה זה:** כלי Visualization.

**מאפיינים:**
- Dashboards יפים
- מתחבר ל-Prometheus, CloudWatch, ועוד
- Alerts
- Open source

---

## NGINX

**מה זה:** Web server רב-תכליתי.

**שימושים:**
- Web Server - מגיש קבצים סטטיים
- Reverse Proxy - מעביר בקשות ל-backend
- Load Balancer - מפזר עומסים
- Ingress Controller - בקוברנטיס

---

# 🌐 API & HTTP

---

## HTTP STATUS CODES

| סדרה | משמעות | דוגמאות |
|------|--------|---------|
| **2xx** | הצלחה | 200 OK, 201 Created, 204 No Content |
| **3xx** | Redirect | 301 Moved, 302 Found, 304 Not Modified |
| **4xx** | שגיאת Client | 400 Bad Request, 401 Unauthorized, 404 Not Found |
| **5xx** | שגיאת Server | 500 Internal Error, 502 Bad Gateway, 503 Unavailable |

---

## 4 סוגי קריאות API (CRUD)

| Method | פעולה | דוגמה |
|--------|-------|-------|
| **GET** | Read - קריאה | GET /users/123 |
| **POST** | Create - יצירה | POST /users |
| **PUT/PATCH** | Update - עדכון | PUT /users/123 |
| **DELETE** | Delete - מחיקה | DELETE /users/123 |

---

## REST API vs SOAP API

| מאפיין | REST | SOAP |
|--------|------|------|
| **פורמט** | JSON (בד"כ) | XML בלבד |
| **פרוטוקול** | HTTP | HTTP, SMTP, TCP |
| **משקל** | קל | כבד |
| **שימוש** | Web, Mobile | Enterprise, Banking |

---

# 🏛️ ARCHITECTURE

---

## MICROSERVICES vs MONOLITH

| מאפיין | Monolith | Microservices |
|--------|----------|---------------|
| **מבנה** | אפליקציה אחת גדולה | שירותים קטנים |
| **פריסה** | הכל ביחד | כל שירות בנפרד |
| **Scaling** | הכל או כלום | לפי שירות |
| **צוות** | קטן | מרובים |
| **Complexity** | פשוט להתחיל | מורכב לנהל |

**מתי Monolith:** MVP, צוות קטן, domain פשוט

**מתי Microservices:** מוצר בוגר, צוותים מרובים, scale שונה

---

## EC2 vs KUBERNETES

| מתי EC2 | מתי Kubernetes |
|---------|----------------|
| אפליקציה פשוטה | Microservices |
| צוות בלי ניסיון K8s | צוות עם ידע |
| Stateful legacy | Cloud Native |
| עלות נמוכה חשובה | Scalability חשובה |

---

## HANDLER

**מה זה:** פונקציה שמטפלת בבקשה/אירוע.

**דוגמה ב-Lambda:**
```python
def handler(event, context):
    return {"statusCode": 200}
```

---

# 📋 סביבות

---

## TEST vs STAGING vs PROD

| סביבה | מטרה | נתונים | משאבים |
|-------|------|--------|--------|
| **Dev/Test** | בדיקות מפתחים | מזויפים | קטנים |
| **Staging** | Pre-production | אנונימיים | כמו Prod |
| **Production** | משתמשים אמיתיים | אמיתיים | מלאים |

---

# 🎯 תרחישים

---

## תרחיש: הקמת אתר E-Commerce

**שאלות לשאול:**

1. **גאוגרפיה** - ישראל בלבד? → Region il-central-1. גלובלי? → CloudFront

2. **עדכניות מוצרים** - לעיתים רחוקות? → Redis caching

3. **כמות כניסות** - לפי זה: Auto Scaling + DB sizing

---

## תרחיש: קמפיין חגים (10K→40K)

**פתרון:**

1. **Auto Scaling** - CPU > 70% → הוסף instances
2. **Read Replicas** - DB נוסף לקריאות
3. **Caching** - Redis
4. **Pre-warming** - העלה instances מראש

---

## תרחיש: שדרוג K8s Cluster

**שלבים:**

1. **Control Plane קודם** - חייב להיות מתקדם מ-Workers
2. **בדיקה** - ודא שהכל תקין
3. **Worker Nodes** - אחד-אחד (drain → upgrade → uncordon)
4. **חזור** - max 2 minor versions בכל פעם

---

## תרחיש: Pods ב-ERROR

**שלבים לדיבוג:**

```bash
kubectl describe pod <name>  # High level - K8s issues
kubectl logs <name>          # App level - Application issues
```

**סיבות נפוצות:**
- ImagePullBackOff - אין גישה ל-Registry
- CrashLoopBackOff - האפליקציה קורסת
- OOMKilled - חוסר זיכרון
- Permissions - חוסר הרשאות

---

## תרחיש: Traffic מ-ALB ל-K8s

**ברמת ALB:**
- Public Subnet
- SG: Inbound 80, 443 from 0.0.0.0/0
- Redirect 80 → 443
- אופציונלי: WAF

**ברמת K8s:**
- SG Referencing - רק ALB SG
- Ingress - חוקי ניתוב
- Ingress Controller - אכיפה

---

## תרחיש: K8s בלי אינטרנט

**בעיות:**
- לא יכול לעשות Pull ל-Images
- לא יכול להתקין packages

**פתרונות:**
- Private Registry (ECR + VPC Endpoint)
- Golden AMI - Images מוכנים
- Private Link - גישה לשירותי AWS

---

## תרחיש: Scaling DB בלי Downtime

**Aurora:**
- Auto Scaling אוטומטי
- Cross-Region reads

**RDS רגיל - Vertical:**
1. צור Standby ב-AZ אחר
2. שדרג את ה-Standby
3. Failover (30-60 שניות)

**RDS - Horizontal:**
- הוסף Read Replicas
- Middleware לניתוב queries

**טיפ:** RDS Proxy מחזיק חיבורים בזמן Failover

---

</div>
