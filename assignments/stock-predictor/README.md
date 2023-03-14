# stock-predictor
Stock Prophet

## Week 12 - MLOps 0

<img src="img/week-12-MLOps0-screenshot-1.png" alt="drawing" width="400"/>

<h3>
How does the Prophet Algorithm differ from an LSTM?
Why does an LSTM have poor performance against ARIMA and Profit for Time Series?
</h3>

Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

A few reasons an LSTM may have poor performance compared to ARIMA and Profit for time series are Lack of sufficient training data, Poor hyperparameter tuning, Overfitting, Stationarity and Complexity.

<h3>
What is exponential smoothing and why is it used in Time Series Forecasting?
</h3>

Exponential smoothing is a method for smoothing time series data using the exponential function. It is a type of moving average (MA) smoothing where weights decrease exponentially as observations come from further in the past, the smallest weights are associated with the oldest observations.

<h3>
What is stationarity? What is seasonality? Why Is Stationarity Important in Time Series Forecasting?
</h3>

Stationarity is a property of a stochastic process that is independent of time. A stationary process has a constant mean and variance, and is autocorrelated only at zero lag. Seasonality is the presence of variations that occur at specific regular intervals less than a year, such as weekly, monthly, or quarterly.

<h3>
How is seasonality different from cyclicality? Fill in the blanks:
</h3>

Seasonality is predictable, whereas cyclicality is not.
Seasonality refers to a repeating pattern within a period of one year or less, while cyclicality refers to a repeating pattern over a period longer than one year. The two patterns are different in terms of their duration, underlying causes, and the way they affect time series data.
Another key difference between seasonality and cyclicality is that seasonality is often driven by external factors such as the weather, while cyclicality is driven by internal factors such as changes in consumer and investor behavior.

## Week 13 - Containers

<img src="img/week-13-containers-screenshot-1.png" alt="drawing" width="400"/>

<h3>
What does it mean to create a Docker image and why do we use Docker images?
</h3>

A Docker image is a file that is used to execute code in a Docker container. Docker images are used to package an application and its dependencies into a standardized unit for software development. Docker images are also used to create Docker containers.

<h3>
Please explain what is the difference from a Container vs a Virtual Machine?
</h3>

A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A virtual machine (VM) is an emulation of a computer system. Virtual machines are based on computer architectures and provide functionality of a physical computer. Their implementations may involve specialized hardware, software, or a combination.

<h3>
What are 5 examples of container orchestration tools (please list tools)?
</h3>

Kubernetes, Docker Swarm, Amazon ECS, Azure Container Service, Google Kubernetes Engine.

<h3>
How does a Docker image differ from a Docker container?
</h3>

A Docker image is a file that is used to execute code in a Docker container. Docker images are used to package an application and its dependencies into a standardized unit for software development. Docker images are also used to create Docker containers. A Docker container is a runtime instance of a Docker image. Docker containers are used to run applications by packaging up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.