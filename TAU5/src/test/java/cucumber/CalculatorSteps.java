package cucumber;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class CalculatorSteps {
    private WebDriver driver = new ChromeDriver();

    @Given("Page with calculator")
    public void page_with_calculator() {
        String chromeDriverPath = System.getenv("WEBDRIVER_CHROME_DRIVER");
        System.getProperty("webdriver.chrome.driver", chromeDriverPath);
        driver.get("https://kalkulatorprocentow.pl");
    }
    @When("User tries to enter his calculation data")
    public void user_tries_to_enter_his_calculation_data() {
        driver.findElement(By.id("percent")).sendKeys("5");
        driver.findElement(By.id("percentValue")).sendKeys("3");
        driver.findElement(By.xpath("//*[@id=\"p1\"]/div[1]/div[5]/button[1]")).click();
    }
    @Then("User should received result of the calculation")
    public void user_should_received_result_of_the_calculation() {
        final var expectedErrorMessage = "0.15";
        try {
            Thread.sleep(1000);
            final var result = driver.findElement(By.id("percentResult"));
            final var actualResultMessage = result.getText();

            if (actualResultMessage.equals(expectedErrorMessage)) {
                System.out.println("Correct result");
            } else {
                System.out.println("Incorrect result. Should be " + expectedErrorMessage);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}