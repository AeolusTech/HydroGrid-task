# HydroGrid-task

Task A


## App type
* URL-shortener
* HydroGrid backend

## Requirements
* ~100 requests per second
* spikes from 200-1000 requests per second
* accessible by anyone and served public
* HA

## Hosted app (PoC)
* URL-shortener app on MIT license: https://github.com/amitt001/pygmy

# Solution no. 1 (new tech :D)

## Architecture suggestions
* Separate frontend from backend into different deployments
** it will be likely the backend might have to be replicated, whereas the frontend not

### Database
* NoSQL database could be scaled horizontally (just add more servers), whereas SQL requires a bit downtime
* NewSQL would supply the benefits of relational database and also provide horizontal scaling.
** Quote: "Vitess has been a core component of YouTube's database infrastructure since 2011, and has grown to encompass tens of thousands of MySQL nodes.". It has Apache Version 2.0 license."
** https://benchmark.vitess.io/cron done on m2.xlarge.x86. $ 1,460.00 USD

### Server setup
* requires Go to be present on the server

### Monitoring

## Verification

### Integration

### Deployment

### Rollback

### Alerting
Prometheus will handle that.

### Monitoring
Prometheus will handle that.

### Increase in load

#### 2x or 10x

Vitess can be horizontally scaled


# Solution no. 2 (old way)

## Architecture suggestions

### Database
* PostgreSQL if we are planning to do some operations on the Database and we want a more secure solution
* SQLite if it's just to save the data

### Server setup

### Monitoring

## Verification

### Integration

### Deployment

### Rollback

### Alerting
Same as solution no. 1

### Monitoring
Same as solution no. 1

### Increase in load

#### 2x or 10x

1. Spin up second/bigger db
2. copy the data manually and et voilla