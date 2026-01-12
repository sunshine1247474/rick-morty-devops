<div dir="rtl" align="right">

# 🎯 DevOps Interview Q&A - מאגר שאלות ותשובות לראיון

> מבוסס על כל ה-PDFs מהקורס. תשאל אותי כל שאלה ואני אענה בצורה ברורה וטבעית!

---

# ☁️ AWS - Amazon Web Services

## AWS Basics (הקדמה)

### ❓ "מה זה AWS?"

AWS זה ספק ענן של אמזון - הגדול בעולם. במקום לקנות שרתים פיזיים, אתה שוכר משאבים לפי שימוש. יש להם מעל 200 שירותים - מחשוב, אחסון, רשת, בסיסי נתונים, AI ועוד.

### ❓ "מה זה Region ו-Availability Zone?"

**Region** = אזור גאוגרפי (למשל: us-east-1, eu-west-1, il-central-1).
**AZ** = מרכז נתונים בתוך Region. לכל Region יש לפחות 2-3 AZs.

למה חשוב? **High Availability** - אם AZ אחד נופל, השני ממשיך לעבוד.

### ❓ "מה השירותים העיקריים ב-AWS?"

- **EC2** - שרתים וירטואליים
- **S3** - אחסון אובייקטים
- **RDS** - בסיסי נתונים
- **VPC** - רשתות וירטואליות
- **Lambda** - Serverless
- **EKS** - Kubernetes מנוהל
- **IAM** - ניהול זהויות והרשאות

---

## EC2 - Elastic Compute Cloud

### ❓ "מה זה EC2?"

EC2 זה שרת וירטואלי בענן. אתה בוחר גודל (CPU, RAM), מערכת הפעלה, ומשלם לפי שעה או שנייה.

### ❓ "מה זה Instance Type?"

סוג המכונה שאתה בוחר. לכל אחד יחס שונה של CPU/Memory:

| Family | שימוש | דוגמה |
|--------|-------|-------|
| **t** | General purpose, burstable | t3.micro, t3.medium |
| **m** | General purpose, balanced | m5.large |
| **c** | Compute optimized | c5.xlarge |
| **r** | Memory optimized | r5.2xlarge |
| **g/p** | GPU | g4dn.xlarge |

**הקונבנציה:** `t3.micro` = Family(t) + Generation(3) + Size(micro)

### ❓ "מה ההבדל בין On-Demand, Reserved, Spot?"

| סוג | תשלום | הנחה | מתי להשתמש |
|-----|-------|------|------------|
| **On-Demand** | לפי שעה | 0% | Dev, testing, unpredictable |
| **Reserved** | התחייבות 1-3 שנים | עד 72% | Production, steady workloads |
| **Spot** | מכירה פומבית | עד 90% | Batch jobs, flexible (יכול להיפסק!) |
| **Dedicated** | שרת פיזי שלם | תלוי | Compliance, licensing |

### ❓ "מה זה AMI?"

**AMI** (Amazon Machine Image) = תמונת מכונה. זה כמו "צילום" של שרת עם מערכת הפעלה ותוכנות מותקנות. אתה יכול ליצור AMI משלך ולהשתמש בו שוב ושוב.

### ❓ "מה זה Security Group?"

**Security Group** = Firewall וירטואלי לEC2. מגדיר:
- **Inbound** - מה מותר להיכנס
- **Outbound** - מה מותר לצאת

ברירת מחדל: Inbound חסום, Outbound פתוח.

---

## IAM - Identity and Access Management

### ❓ "מה זה IAM?"

מערכת ניהול זהויות והרשאות. שולטת במי יכול לעשות מה ב-AWS.

### ❓ "מה ההבדל בין User, Group, Role?"

| רכיב | מיועד ל | דוגמה |
|------|---------|-------|
| **User** | אדם ספציפי | developer@company.com |
| **Group** | קבוצת Users | "Developers", "Admins" |
| **Role** | שירותים/אפליקציות | EC2 שניגש ל-S3 |

### ❓ "מה זה Policy?"

מסמך JSON שמגדיר הרשאות. מכיל:
- **Effect**: Allow / Deny
- **Action**: מה מותר (s3:GetObject)
- **Resource**: על מה (arn:aws:s3:::mybucket/*)

---

## VPC - Virtual Private Cloud

### ❓ "מה זה VPC?"

רשת וירטואלית פרטית שלך ב-AWS. אתה מגדיר את טווח ה-IPs, מחלק ל-Subnets, ושולט בתנועה.

### ❓ "מה זה CIDR?"

**CIDR** = שיטה להגדרת טווח כתובות IP.
- `10.0.0.0/16` = 65,536 כתובות
- `10.0.1.0/24` = 256 כתובות
- ככל שהמספר אחרי ה-/ גדול יותר, פחות כתובות.

### ❓ "מה זה Subnet?"

חלוקה של ה-VPC לתת-רשתות. שני סוגים:
- **Public** - יש גישה לאינטרנט (Web servers)
- **Private** - אין גישה ישירה (Databases)

### ❓ "מה זה Internet Gateway?"

שער שמחבר את ה-VPC לאינטרנט. בלעדיו, אף אחד לא יכול להיכנס או לצאת.

### ❓ "מה זה NAT Gateway?"

מאפשר לשרתים ב-Private Subnet לצאת לאינטרנט (לעדכונים, APIs) בלי להיחשף לתנועה נכנסת.

### ❓ "מה זה NACL?"

**Network ACL** = Firewall ברמת ה-Subnet. Stateless - צריך להגדיר גם Inbound וגם Outbound.

לעומת Security Group שהוא Stateful - אם הכנסת, התשובה יוצאת אוטומטית.

### ❓ "מה זה VPC Peering?"

חיבור בין שני VPCs. מאפשר לתקשר ביניהם כאילו הם רשת אחת.

### ❓ "מה זה Private Link / VPC Endpoint?"

גישה לשירותי AWS בלי לעבור דרך האינטרנט. יותר מאובטח ומהיר.

---

## S3 - Simple Storage Service

### ❓ "מה זה S3?"

אחסון אובייקטים (קבצים) ללא הגבלה. לא דיסק רגיל - אתה שם ומושך קבצים דרך API.

### ❓ "מה זה Bucket?"

"דלי" שמכיל את האובייקטים. השם חייב להיות ייחודי גלובלית!

### ❓ "מה ה-Storage Classes?"

| Class | זמינות | מחיר | שימוש |
|-------|--------|------|-------|
| **Standard** | מיידי | גבוה | גישה תכופה |
| **IA** | מיידי | נמוך יותר | גישה לא תכופה |
| **Glacier** | דקות-שעות | זול | ארכיון |
| **Glacier Deep** | 12-48 שעות | הכי זול | ארכיון ארוך טווח |

### ❓ "מה זה Versioning?"

שמירת גרסאות של כל קובץ. אם מחקת בטעות - אפשר לשחזר.

---

## EBS & EFS - Storage

### ❓ "מה זה EBS?"

**EBS** (Elastic Block Store) = דיסק וירטואלי שמתחבר ל-EC2. כמו דיסק קשיח רגיל.

### ❓ "מה ההבדל בין EBS ל-EFS?"

| מאפיין | EBS | EFS |
|--------|-----|-----|
| סוג | Block (דיסק) | File (NFS) |
| חיבור | EC2 אחד | מרובה EC2 |
| AZ | באותו AZ | Cross-AZ |
| Scaling | ידני | אוטומטי |
| שימוש | Database | Shared files |

---

## Load Balancer & Auto Scaling

### ❓ "מה זה Load Balancer?"

מפזר תנועה בין מספר שרתים. מונע עומס יתר על שרת אחד.

### ❓ "מה הסוגים של Load Balancer?"

| סוג | שכבה | שימוש |
|-----|------|-------|
| **ALB** | Layer 7 (HTTP) | Web apps, path routing |
| **NLB** | Layer 4 (TCP) | Gaming, high performance |
| **GLB** | Layer 3 | Firewalls |

### ❓ "מה זה Auto Scaling Group?"

קבוצת EC2 שגדלה וקטנה אוטומטית לפי עומס. מגדירים:
- **Min** - מינימום instances
- **Max** - מקסימום instances
- **Desired** - כמות רצויה
- **Scaling Policy** - מתי להוסיף/להוריד (CPU > 70%)

---

## RDS - Relational Database Service

### ❓ "מה זה RDS?"

בסיס נתונים מנוהל. AWS מטפל ב-backups, patching, HA. אתה רק משתמש.

### ❓ "מה זה Multi-AZ?"

העתק של ה-DB ב-AZ אחר. אם ה-Primary נופל - Failover אוטומטי ל-Standby.

### ❓ "מה זה Read Replica?"

עותק לקריאה בלבד. מוריד עומס מה-Primary, משפר ביצועים.

### ❓ "מה זה Aurora?"

בסיס נתונים של AWS - תואם MySQL/PostgreSQL אבל 5x מהיר יותר. Auto-scaling, Global Database.

---

## Lambda - Serverless

### ❓ "מה זה Lambda?"

מריץ קוד בלי לנהל שרתים. אתה מעלה פונקציה, היא רצה כשיש trigger.

### ❓ "איך Lambda עובד?"

1. מגדיר Trigger (API Gateway, S3, EventBridge...)
2. הקוד רץ
3. משלם רק על זמן הריצה (milliseconds)

### ❓ "מה המגבלות?"

- **Timeout**: עד 15 דקות
- **Memory**: עד 10GB
- **Storage**: 512MB (10GB עם EFS)

### ❓ "מה זה EventBridge?"

שירות שמתזמן Lambda:
- **Cron**: "כל יום ב-2 בלילה"
- **Rate**: "כל 5 דקות"
- **Events**: תגובה לאירועים ב-AWS

---

## Route 53 - DNS

### ❓ "מה זה Route 53?"

שירות DNS של AWS. מתרגם domain names לכתובות IP.

### ❓ "מה הם סוגי הניתוב?"

| סוג | לוגיקה |
|-----|--------|
| **Simple** | IP אחד |
| **Weighted** | לפי אחוזים |
| **Latency** | לפי מהירות |
| **Geolocation** | לפי מיקום המשתמש |
| **Failover** | Primary/Secondary |

---

## CloudWatch & CloudTrail

### ❓ "מה זה CloudWatch?"

מערכת Monitoring של AWS:
- **Metrics** - CPU, Memory, Network
- **Logs** - לוגים מכל מקום
- **Alarms** - התראות
- **Dashboards** - גרפים

### ❓ "מה זה CloudTrail?"

מתעד כל פעולה ב-AWS account. מי עשה מה ומתי. לאבטחה ו-audit.

---

## CloudFront - CDN

### ❓ "מה זה CloudFront?"

CDN של AWS. מפיץ תוכן ל-Edge Locations ברחבי העולם. מוריד latency למשתמשים רחוקים.

### ❓ "איך זה עובד?"

1. משתמש מבקש קובץ
2. CloudFront בודק אם יש ב-cache
3. אם לא - מביא מה-Origin (S3, EC2)
4. שומר ב-cache לפעם הבאה

---

## CloudFormation

### ❓ "מה זה CloudFormation?"

Infrastructure as Code של AWS. כותבים YAML/JSON, מקבלים תשתית.

### ❓ "מה ההבדל מ-Terraform?"

| CloudFormation | Terraform |
|----------------|-----------|
| AWS בלבד | Multi-cloud |
| AWS מנהל State | אתה מנהל |
| JSON/YAML | HCL |

---

# ☸️ Kubernetes

## Architecture

### ❓ "מה זה Kubernetes?"

מערכת לניהול Containers. מפרוסת, מנטרת, מסקיילת אוטומטית.

### ❓ "מה המבנה של Cluster?"

**Control Plane** (Master):
- **API Server** - הכניסה לכל פעולה
- **etcd** - Database שמאחסן את ה-state
- **Scheduler** - מחליט איפה לשים Pods
- **Controller Manager** - מוודא שהמצב הרצוי = המצב בפועל

**Worker Nodes**:
- **Kubelet** - Agent שמריץ Pods
- **Kube-proxy** - Networking
- **Container Runtime** - Docker/containerd

### ❓ "מה זה etcd?"

Key-value store שמאחסן את כל המידע של הקלאסטר. אם etcd נופל - אין קלאסטר.

### ❓ "מה עושה ה-Scheduler?"

מחליט על איזה Node לשים Pod חדש. בודק:
- Resources פנויים
- Taints & Tolerations
- Affinity rules

### ❓ "מה עושה ה-Kubelet?"

Agent על כל Node. מקבל הוראות מה-API Server ומוודא שה-Pods רצים.

---

## Core Concepts

### ❓ "מה זה Pod?"

היחידה הקטנה ביותר ב-K8s. מכיל Container אחד או יותר שחולקים Network ו-Storage.

### ❓ "מה זה Deployment?"

מנהל Pods עם:
- מספר Replicas
- Rolling Updates
- Rollback

### ❓ "מה זה ReplicaSet?"

שומר על מספר קבוע של Pods. Deployment יוצר ReplicaSet.

### ❓ "מה זה Service?"

חושף Pods לתקשורת. סוגים:
- **ClusterIP** - פנימי
- **NodePort** - Port על כל Node
- **LoadBalancer** - LB חיצוני

### ❓ "מה זה Namespace?"

חלוקה לוגית של הקלאסטר. מפריד בין צוותים/סביבות.

---

## Scheduling

### ❓ "מה זה Labels ו-Selectors?"

**Labels** = תגיות על Resources (app: web, env: prod)
**Selectors** = בחירת Resources לפי Labels

### ❓ "מה זה Taints ו-Tolerations?"

**Taint** על Node = "אל תשים עלי Pods"
**Toleration** על Pod = "אני יכול לרוץ על Node עם Taint"

### ❓ "מה זה Node Affinity?"

כללים לבחירת Node. "רוץ רק על Nodes עם SSD"

### ❓ "מה זה Pod Affinity/Anti-Affinity?"

**Affinity** - רוץ ליד Pod מסוים
**Anti-Affinity** - רוץ רחוק מ-Pod מסוים

---

## Workload Types

### ❓ "מה ההבדל בין Deployment, StatefulSet, DaemonSet?"

| סוג | שימוש | דוגמה |
|-----|-------|-------|
| **Deployment** | Stateless apps | Web server |
| **StatefulSet** | Stateful, זהות קבועה | Database |
| **DaemonSet** | Pod על כל Node | Logging agent |

---

## Configuration

### ❓ "מה זה ConfigMap?"

אחסון configuration לא-רגיש. Environment variables, config files.

### ❓ "מה זה Secret?"

כמו ConfigMap אבל למידע רגיש. Passwords, API keys. מוצפן base64 (לא הצפנה אמיתית!).

---

## Lifecycle Management

### ❓ "מה זה Rolling Update?"

עדכון הדרגתי - מחליף Pod אחד בכל פעם. Zero downtime.

### ❓ "מה זה Rollback?"

חזרה לגרסה קודמת: `kubectl rollout undo deployment/myapp`

---

## Networking

### ❓ "מה זה Ingress?"

ניתוב HTTP/HTTPS לתוך הקלאסטר. מגדיר hosts ו-paths.

### ❓ "מה זה Ingress Controller?"

התוכנה שמבצעת את הניתוב. NGINX, Traefik, HAProxy.

### ❓ "מה זה CNI?"

Container Network Interface. Plugins לניהול רשת: Calico, Flannel.

### ❓ "מה זה CoreDNS?"

DNS פנימי של הקלאסטר. מתרגם שמות Services ל-IPs.

---

## Health & Probes

### ❓ "מה זה Liveness Probe?"

בודק "האם ה-Container חי?" אם לא - Restart.

### ❓ "מה זה Readiness Probe?"

בודק "האם מוכן לקבל Traffic?" אם לא - לא שולחים בקשות.

---

## Scaling

### ❓ "מה זה HPA?"

Horizontal Pod Autoscaler - מוסיף/מוריד Pods לפי metrics (CPU, memory).

### ❓ "מה זה Cluster Autoscaler?"

מוסיף/מוריד Nodes לקלאסטר.

---

## Storage

### ❓ "מה זה PV ו-PVC?"

**PV** (Persistent Volume) = האחסון הפיזי
**PVC** (Persistent Volume Claim) = בקשה לאחסון

---

# 🐳 Docker

## Basics

### ❓ "מה זה Docker?"

פלטפורמה להרצת Containers. מבודד אפליקציות עם כל התלויות שלהן.

### ❓ "מה ההבדל בין Container ל-VM?"

| Container | VM |
|-----------|-----|
| חולק Kernel | Kernel משלו |
| קל (MBs) | כבד (GBs) |
| מהיר לעלות | איטי |
| פחות בידוד | בידוד מלא |

### ❓ "מה זה Image?"

תבנית לContainer. מכילה OS, קוד, תלויות. Read-only.

### ❓ "מה זה Dockerfile?"

קובץ עם הוראות לבניית Image.

---

## Advanced

### ❓ "מה זה Multi-Stage Build?"

בניית Image בשלבים. Stage 1 = Build, Stage 2 = Run. Image סופי קטן יותר.

### ❓ "מה זה Docker Compose?"

כלי להרצת מספר Containers יחד. קובץ YAML אחד.

### ❓ "מה ההבדל בין Volume ל-Bind Mount?"

**Volume** - Docker מנהל (Production)
**Bind Mount** - תיקייה מהמחשב (Development)

### ❓ "Docker Networking?"

| Type | שימוש |
|------|-------|
| bridge | ברירת מחדל |
| host | רשת של ה-host |
| none | ללא רשת |

---

# 🔧 Terraform

### ❓ "מה זה Terraform?"

Infrastructure as Code. כותבים קוד, מקבלים תשתית בענן.

### ❓ "מה זה State?"

קובץ שמתעד את המצב הנוכחי. Terraform משווה State למה שרוצים.

### ❓ "מה זה Drift?"

פער בין State למצב האמיתי. קורה כששינו ידנית.

### ❓ "מה זה Module?"

קוד לשימוש חוזר. כמו פונקציה.

### ❓ "מה זה Workspace?"

States נפרדים לאותו קוד (dev, prod).

---

# 🔄 CI/CD

### ❓ "מה זה CI?"

**Continuous Integration** - Build ו-Test אוטומטי על כל commit.

### ❓ "מה זה CD?"

**Continuous Delivery/Deployment** - פריסה אוטומטית לסביבות.

### ❓ "מה ההבדל בין GitHub Actions ל-Jenkins?"

| GitHub Actions | Jenkins |
|----------------|---------|
| SaaS | Self-hosted |
| קל להתחיל | גמיש יותר |
| YAML | Groovy |

---

# 🐧 Linux

## Basic Commands

### ❓ "פקודות בסיסיות?"

| פקודה | תפקיד |
|-------|-------|
| `ls` | רשימת קבצים |
| `cd` | החלפת תיקייה |
| `pwd` | תיקייה נוכחית |
| `cp` | העתקה |
| `mv` | העברה/שינוי שם |
| `rm` | מחיקה |
| `mkdir` | יצירת תיקייה |
| `cat` | הצגת תוכן קובץ |

### ❓ "מה זה File Permissions?"

`-rwxr-xr--` = Owner(rwx) Group(r-x) Others(r--)
- **r** = read (4)
- **w** = write (2)
- **x** = execute (1)

`chmod 755 file` = Owner: all, Others: read+execute

### ❓ "מה ההבדל בין Hard Link ל-Soft Link?"

**Hard Link** - מצביע לאותו inode. מחיקת המקור לא משפיעה.
**Soft Link** - קיצור דרך. מחיקת המקור שובר את הקישור.

---

## Text Processing

### ❓ "מה עושה grep?"

מחפש טקסט בקבצים: `grep "error" logfile.txt`

### ❓ "מה עושה awk?"

עיבוד טקסט מתקדם: `awk '{print $1, $3}' file` - מדפיס עמודות 1 ו-3

### ❓ "מה עושה sed?"

עריכת טקסט: `sed 's/old/new/g' file` - מחליף טקסט

---

## System Administration

### ❓ "איך בודקים שימוש בדיסק?"

`df -h` - דיסקים מותקנים
`du -sh *` - גודל תיקיות

### ❓ "איך בודקים תהליכים?"

`ps aux` - כל התהליכים
`top` / `htop` - בזמן אמת

### ❓ "איך מנהלים Services?"

```bash
systemctl start nginx
systemctl stop nginx
systemctl status nginx
systemctl enable nginx  # הפעלה אוטומטית בבוט
```

---

# 📊 Monitoring

### ❓ "מה זה Prometheus?"

מערכת Monitoring. אוספת Metrics, מאחסנת Time-series, Alerting.

### ❓ "מה זה Grafana?"

כלי Visualization. יוצר Dashboards יפים מ-Prometheus ואחרים.

### ❓ "מה זה AlertManager?"

מנהל התראות מ-Prometheus. Routing, Silencing, Grouping.

---

# 🌐 Networking

### ❓ "מה זה DNS?"

תרגום שמות לכתובות IP. google.com → 142.250.190.46

### ❓ "מה זה HTTP Status Codes?"

| Range | משמעות |
|-------|--------|
| 2xx | הצלחה |
| 3xx | Redirect |
| 4xx | שגיאת Client |
| 5xx | שגיאת Server |

### ❓ "מה זה REST API?"

סגנון ארכיטקטורה לAPI:
- **GET** - קריאה
- **POST** - יצירה
- **PUT** - עדכון
- **DELETE** - מחיקה

---

**שאל אותי כל שאלה ואני אענה!** 🎯

</div>
