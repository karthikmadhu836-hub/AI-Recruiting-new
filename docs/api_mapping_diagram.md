# AI API Mapping Diagram

```
                   +--------------------+
                   |    Frontend UI     |
                   +---------+----------+
                             |
                             |
                     HTTPS / REST APIs
                             |
                   +---------v----------+
                   |    Backend API     |
                   +---------+----------+
                             |
      -------------------------------------------------------
      |          |          |          |          |          |
      |          |          |          |          |          |
+-----v----+ +---v----+ +---v----+ +---v----+ +---v----+ +---v----+
| Resume   | | ATS    | |Screen- | | HR AI  | |Technical| |Decision|
| Parser   | | Score  | | ing AI | |        | | AI      | | Engine |
+----------+ +--------+ +--------+ +--------+ +---------+ +--------+
      |          |          |          |          |          |
      --------------------------------------------------------
                             |
                    Cross-Round Engine
                             |
                     Hiring Report Engine
                             |
                   +---------v----------+
                   |     Database       |
                   +--------------------+
```

## API Endpoints

| API | Endpoint |
|------|----------|
| Resume Parser | `/resume/parse` |
| ATS Score | `/ats/score` |
| Screening | `/screening/run` |
| HR Interview | `/interview/run` |
| Technical | `/technical/run` |
| Machine Test | `/machine/evaluate` |
| Decision | `/decision/final` |
| Report | `/report/generate` |