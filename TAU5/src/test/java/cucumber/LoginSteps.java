package cucumber;

import io.cucumber.java.en.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class LoginSteps {
    private WebDriver driver = new ChromeDriver();
    private WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(2));

    @Given("Login page")
    public void login_page() {
        String chromeDriverPath = System.getenv("WEBDRIVER_CHROME_DRIVER");
        System.getProperty("webdriver.chrome.driver", chromeDriverPath);
        driver.get("https://www.reddit.com/login/");
    }
    @When("User tries to enter his login data")
    public void user_tries_to_enter_his_login_data() {
        driver.findElement(By.id("loginUsername")).sendKeys("username");
        driver.findElement(By.id("loginPassword")).sendKeys("password");
        final var loginBtn = driver.findElement(By.xpath("//button[@class='AnimatedForm__submitButton m-full-width']"));

        loginBtn.click();
    }
    @Then("He should received that data is wrong")
    public void he_should_received_that_data_is_wrong() {
        final var expectedErrorMessage = "Incorrect username or password";
        try {
            Thread.sleep(1000);
            final var error = wait.until(ExpectedConditions.presenceOfElementLocated(By.className("AnimatedForm__errorMessage")));
            final var actualErrorMessage = error.getText();

            if (actualErrorMessage.equals(expectedErrorMessage)) {
                System.out.println("Error message is as expected.");
            } else {
                System.out.println("Error message is not as expected.");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
